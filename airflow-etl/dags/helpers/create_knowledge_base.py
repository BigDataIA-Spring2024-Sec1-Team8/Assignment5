import csv
from pinecone import Pinecone, ServerlessSpec
import numpy as np
import re
import openai
from tqdm import tqdm
import os
from openai import OpenAI
openai.api_key = os.getenv('OPENAI_KEY')
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

def generate_technical_note(los, summary, introduction):
    context = f"""Given the Learning Outcome Statement (LOS) provided below, create a technical note that summarizes the key points. Include tables, figures, and equations as necessary to enhance clarity and understanding. 
    Don't use external knowledge
    Learning Outcome Statement (LOS):
    {los}

    Summary:
    {summary}

    Introduction:
    {introduction}
    """
    prompt = f"""
    create a technical note which is Summary of topic in context and summary should be not more than 10 sentences.
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"system": context},
            {"user": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
def generate_markdown(topic, technical_note):
    intro = topic["Introduction"]
    summary = topic["Summary"]
    learning_outcomes = topic["LOS"]

    # Generate Markdown document
    markdown_content = f"# Introduction\n\n{intro}\n\n## Summary\n\n{summary}\n\n## Learning Outcomes\n\n{learning_outcomes}\n\n## Technical Note\n\n{technical_note}"

    # Write the Markdown content to a file
    with open(f'markdowns/{topic["name"]}.md', "w") as md_file:
        md_file.write(markdown_content)



def generate_embedding(text_to_embed):
    model_name = "text-embedding-3-large"

    response = openai.embeddings.create(
        model=model_name,
        input=text_to_embed,
        encoding_format="float"  # Adjust format if needed (e.g., "json")
    )
    # embedding_vector = np.array(base64.b64decode(response.data[0].embedding))
    return response.data[0].embedding

def chunk_markdown(markdown_text):
    # Split by headers (##)
    chunks = re.split(r'##\s+', markdown_text)
    return [chunk.strip() for chunk in chunks if chunk.strip()]

def store_in_pinecone(embeddings, chunk_ids, meta):
    index_name = "note-index"
    # Create index if not exists
    if index_name not in pc.list_indexes().names():
        pc.create_index(name=index_name, dimension=1, spec=spec)

    index = pc.Index(index_name)
    
    index.upsert(vectors=list(zip(chunk_ids, embeddings,meta)), namespace='knowledge')
def remove_non_ascii(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)
def create_markdown(topic):
    dags = os.path.join(os.getcwd(), 'dags')
    res_path = os.path.join(dags, 'resources')
    res_path = os.path.join(res_path, 'markdowns')
    file_path = os.path.join(res_path, f"{topic['name']}.md")
    if not os.path.exists(file_path):
        print("not exists")
        generate_markdown(topic=topic, 
                      technical_note=generate_technical_note(
                          los = topic['LOS'], 
                          summary = topic['Summary'],
                          introduction = topic['Introduction']
                          ))

def process_markdown_topic(topic):
    dags = os.path.join(os.getcwd(), 'dags')
    res_path = os.path.join(dags, 'resources')
    res_path = os.path.join(res_path, 'markdowns')
    file_path = os.path.join(res_path, f"{topic['name']}.md")
    markdown_text = ""
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()
    chunks = chunk_markdown(markdown_text)
    chunk_embeddings = [generate_embedding(chunk) for chunk in chunks]
    chunk_ids = [f"{remove_non_ascii(topic['name'])}_chunk_{i}" for i in range(len(chunks))]
    meta = [{'text': line} for line in chunks]
    store_in_pinecone(chunk_embeddings, chunk_ids, meta)
    
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

# Main function
def create_technical_note(run_id,csv_file):
    dags = os.path.join(os.getcwd(), 'dags')
    res_path = os.path.join(dags, 'resources')
    res_path = os.path.join(res_path, str(run_id))
    # csv_file_s = 'processed.csv'
    c1 = os.path.join(res_path,csv_file)
    
    topics = read_csv(c1)

    # Store LOS and note into Pinecone
    for i in tqdm(range(len(topics))):
        topic = topics[i]        
        create_markdown(topic)

def process_markdown(run_id,csv_file):
    dags = os.path.join(os.getcwd(), 'dags')
    res_path = os.path.join(dags, 'resources')
    res_path = os.path.join(res_path, str(run_id))
    # csv_file_s = 'processed.csv'
    c1 = os.path.join(res_path,csv_file)
    
    topics = read_csv(c1)

    # Store LOS and note into Pinecone
    for i in tqdm(range(len(topics))):
        topic = topics[i]        
        process_markdown_topic(topic)