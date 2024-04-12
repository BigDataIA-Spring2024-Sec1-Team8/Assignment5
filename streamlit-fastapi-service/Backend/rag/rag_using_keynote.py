from pinecone import Pinecone
import openai
from openai import OpenAI
import os
from config_parser import fetch_config
config_path = os.environ.get("CONFIG_PATH")

config = fetch_config(config_path)

openai.api_key = config['keys']['OPENAI_KEY']
client = OpenAI(
api_key = config['keys']['OPENAI_KEY']
)
pc = Pinecone(
        api_key=config['keys']['PINECONE_KEY']
    )

async def generate_answer_using_ai(question,question_answers_string):
    context = f"""Information to answer above question :

    {question_answers_string}
    """
    prompt = f"""
    Generate answers for below question based on following information

    
    {question}

    Don't use external knowledge. Answer in below format:
    Answer: {{answer}}

    Explanation: {{explanation}}
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": context} ,
            {"role": "user", "content": prompt}
        ]
    )

    generated_text = response.choices[0].message.content.strip()
    return generated_text
async def generate_embedding(text_to_embed):
    model_name = "text-embedding-3-large"

    response = openai.embeddings.create(
        model=model_name,
        input=text_to_embed,
        encoding_format="float"  # Adjust format if needed (e.g., "json")
    )
    # embedding_vector = np.array(base64.b64decode(response.data[0].embedding))
    return response.data[0].embedding
async def retrieve_text_from_embedding(embedding):
    # Retrieve the text using the embedding
    response = openai.Embedding.retrieve(embedding=embedding)
    
    # Extract and return the text from the response
    return response["object"]["text"]
async def find_ans_using_knowledge(question, num_matches=3):
    try:
        ques = question.split('Options:**')[0]
        question_vector = await generate_embedding(ques)
        index_name = "note-index"
        index = pc.Index(index_name)
        # Query the Pinecone database
        results = index.query(vector=question_vector, top_k=num_matches,
                               namespace="knowledge", include_values=True,
                               include_metadata=True
                               )

        q_a_string = ""
        for r in results['matches']:
            ques = r['metadata']['text']
            q_a_string+=ques
           
        print("question ", question)
        ansss = await generate_answer_using_ai(question, q_a_string)
        print(ansss)
        return ansss
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

