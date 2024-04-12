import csv
# import openai
from pinecone import Pinecone, ServerlessSpec
import pinecone
import base64
import numpy as np
import re
from openai import OpenAI
import time
from tqdm import tqdm
import openai
import os
openai.api_key = os.getenv('OPENAI_KEY')
# Store LOS and note into Pinecone
client = OpenAI(
api_key = os.getenv('OPENAI_KEY')
)
pc = Pinecone(
        api_key=os.getenv('PINECONE_KEY')
    )
spec=ServerlessSpec(
                cloud='aws',
                region='us-west-2'
            )

# Set up Pinecone


def generate_qas( history=[]):
    prompt = f"""
        Generate question and answer with 4 options with one correct answer from content given in context.Give one unique question which you havent given in chat

        Question: {{your_question}}
        {{4 options}}

        Answer: {{answer}}

        Explanation: {{explanation}}

        """

    history.append({
        "role": "user", "content":prompt
    })
    print("making call", prompt)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=history
    )

    # print(response)
    history.append(
        {"role": "assistant", "content": response.choices[0].message.content.strip()}
    )
    # return response.choices[0].text.strip()
    # Extracting question and answer from the response
    
    generated_text = response.choices[0].message.content.strip()
    question_start = generated_text.find("Question:")
    question_end = generated_text.find("Answer:")
    question = generated_text[question_start:question_end].strip()
    print("--------------")
    print("ques", question)
    answer_start = generated_text.find("Answer: ")
    answer = generated_text[answer_start:].strip()
    print("--------------")
    print("ans", answer)
    return question, answer

def fetch_question_context(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()            
            # start_index = content.find(start_phrase)
            # end_index = content.find(end_phrase, start_index)
            # if start_index == -1 or end_index == -1:
            #     raise ValueError("Start or end phrase not found in the file.")
            extracted_text = content.strip()
            return extracted_text
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# def generate_markdown(topic, technical_note):

def generate_embedding(text_to_embed):
    model_name = "text-embedding-3-large"

    response = openai.embeddings.create(
        model=model_name,
        input=text_to_embed,
        encoding_format="float"  # Adjust format if needed (e.g., "json")
    )
    # embedding_vector = np.array(base64.b64decode(response.data[0].embedding))
    return response.data[0].embedding

def fetch_questions(topic):
    dags = os.path.join(os.getcwd(), 'dags')
    res_path = os.path.join(dags, 'resources')
    topicname=""
    if topic == 'Extensions of Multiple Regression':
        topicname = 'level1.txt'
    elif topic == 'Evaluating Regression Model Fit and Interpreting Model Results':
        topicname = 'level2.txt'
    else:
        topicname = 'level3.txt'

    file_path = os.path.join(res_path, topicname)
    extracted_text = fetch_question_context(file_path)
    if topic == 'Extensions of Multiple Regression':
        extracted_text = extracted_text[extracted_text.find('Answers to Sample Level I Multiple Choice  Questions'):]
    return extracted_text
def store_in_pinecone(embeddings, chunk_ids, meta, namespace):
    index_name = "note-index"
    # Create index if not exists
    if index_name not in pc.list_indexes().names():
        pc.create_index(name=index_name, dimension=1, spec=spec)

    index = pc.Index(index_name)

    # print(list(zip(["test"],[vector])))
    
    index.upsert(vectors=list(zip(chunk_ids, embeddings, meta)), namespace=remove_non_ascii(namespace))

def store_in_csv(topic,questions,answers,suffix):
    zipped_data = zip(questions, answers)
    dags = os.path.join(os.getcwd(), 'dags')
    res_path = os.path.join(dags, 'resources')
    # res_path = os.path.join(res_path, str(run_id))

    csv_file = os.path.join(res_path, f"{topic['name']}_questions_and_answers_{suffix}.csv")
    
    with open(csv_file, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Question', 'Answer'])  # Write header
        writer.writerows(zipped_data)
def remove_non_ascii(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)
def process_topic(run_id,topic, namespace_suffix= ""):
    questions = []
    answers = []
    history = []
    extracted_text = fetch_questions(topic)
    context = f"""
    Give question/answer set to reinforce learning from topic summaries.
            Don't use external knowledge
            Learning Outcome Statement (LOS):
            {topic['LOS']}

            Summary:
            {topic['Summary']}

            Introduction:
            {topic['Introduction']}

        Sample questions and answers

            {extracted_text}

        I want 50 unique question and answer in the format,  one set in each response, considering given sample questions and answer style as an example, don't use topics of above questions. observe only style of asking and difficulty. 

    """
    history.append({
        "role": "system", 
        "content": context})
    prev=-1
    i=0
    while i<50:
        if prev != -1:
            i=prev
        try:
            q,a = generate_qas(history=history)
        except Exception as e:
            prev=i
            time.sleep(60)
            print(str(e))
            continue
        print(q,"\nans\n", a,"\n", i)
        questions.append(q)
        answers.append(a)
        q_embeddings = [generate_embedding(q)]
        a_embeddings = [generate_embedding(a)]
        meta_q = [{"text": q}]
        meta_a = [{"text": a}]
        chunk_ids = [f"{remove_non_ascii(topic['name'])}_question_{i}"]
        print(chunk_ids)
        print(q_embeddings)
        store_in_pinecone(q_embeddings, chunk_ids, meta_q, namespace = f"{topic['name'].replace(' ', '-')}-questions-"+namespace_suffix)
        
        store_in_pinecone(a_embeddings, chunk_ids, meta_a, namespace = f"{topic['name'].replace(' ', '-')}-answers-"+namespace_suffix)
        i+=1
        prev=i
    store_in_csv(topic=topic,questions=questions,answers=answers,suffix=namespace_suffix)
    
    
# Read CSV data
def read_csv(file_path):
    topics = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            topics.append({
                'LOS': row['Learning Outcomes Section'].strip('"'),
                'Summary': row['Summary Bullets'].strip('"'),
                'Introduction': row['Introduction'].strip('"'),
                "name": row['Name of the topic'].strip('"')
            })
    return topics

def generate_qa(run_id,csv_file,namespace_suffix,topic_name ):
    dags = os.path.join(os.getcwd(), 'dags')
    res_path = os.path.join(dags, 'resources')
    res_path = os.path.join(res_path, str(run_id))
    # csv_file_s = 'processed_content.csv'
    c1 = os.path.join(res_path,csv_file)
    # topics = read_csv(c1)
    topics = read_csv(c1)
    # topic_name="Extensions of Multiple Regression"
    # Store LOS and note into Pinecone
    for topic in topics:
        print(topic)
        if topic['name']==topic_name:
            process_topic(run_id,topic, namespace_suffix=namespace_suffix)
            break
    return f"{topic_name}_questions_and_answers_{namespace_suffix}.csv"

