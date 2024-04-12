import csv
# import streamlit as st
from rag.rag_using_qa import find_ans_using_qas
from rag.rag_using_keynote import find_ans_using_knowledge
import re
from download_from_s3 import download_csv_from_s3
from snowflake_wrapper import upload_run
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from websockets.exceptions import ConnectionClosed

csv_file = 'resources/questions_and_answersb.csv'
import time
# Iterate through each question in the CSV file
async def fetch_option(string):
    if not string:
        return None
    pattern = r"Answer:\s*([a-zA-Z])"

    match = re.search(pattern, string)

    if match:
        answer_option = match.group(1)
        # st.write("Answer Option:", answer_option)
        return answer_option
    else:
        # st.write(f"Answer option not found. {string}")
        return None
async def read_questions_from_csv(csv_file,websocket):
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            # Create a CSV reader object
            csv_reader = csv.DictReader(file)
            
            # Iterate through each row in the CSV file
            for row in csv_reader:
                # Extract the question from the 'Question' column
                question = row['Question']
                yield question, row['Answer']
    except FileNotFoundError:
        await websocket.send_json({"message":  f"File '{csv_file}' not found."})
    except Exception as e:
        await websocket.send_json({"message":  f"An error occurred: {e}"})
async def eval1_exec(topic,websocket,run_id):
    total=0
    correct=0
    await download_csv_from_s3(bucket_name="questions-cfa-learning",topic_name=topic)
    csvpath = f'resources/{topic}_setb.csv'
    with open(csvpath, 'r', encoding='utf-8') as file:
            # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        data=[]
            # Iterate through each row in the CSV file
        for row in csv_reader:
            question,real_ans = row['Question'], row['Answer']
            # await websocket.send_json({"message": f"question is:\n:{question}"})
            total+=1
            ans = await find_ans_using_qas(topic,question)
            # await websocket.send_json({"message": f"predicted answer is: \n{ans}"})
            ans_op = await fetch_option(ans)
            # st.write(ans_op)
            real_op = await fetch_option(real_ans)
            # await websocket.send_json({"message": f"real answer is: \n{real_ans}"})
            # st.write(real_op)
            await asyncio.sleep(3)
            data.append({
                "question": question,
                "real": real_ans,
                "predicted": ans
            })
            await websocket.send_json({"table": data})
            if ans_op == real_op:
                correct+=1
    csvpath = f'resources/{topic}_seta.csv'
    with open(csvpath, 'r', encoding='utf-8') as file:
            # Create a CSV reader object
        csv_reader = csv.DictReader(file)
            # Iterate through each row in the CSV file
        for row in csv_reader:
            question,real_ans = row['Question'], row['Answer']
            # await websocket.send_json({"message": f"question is:\n:{question}"})
            total+=1
            ans = await find_ans_using_qas(topic,question)
            # await websocket.send_json({"message": f"predicted answer is: \n{ans}"})
            ans_op = await fetch_option(ans)
            # st.write(ans_op)
            real_op = await fetch_option(real_ans)
            # await websocket.send_json({"message": f"real answer is: \n{real_ans}"})
            # st.write(real_op)
            await asyncio.sleep(3)
            data.append({
                "question": question,
                "real": real_ans,
                "predicted": ans
            })
            await websocket.send_json({"table": data})
            if ans_op == real_op:
                correct+=1
        await upload_run(websocket,run_id,"qa_approach", correct, total,topic)

        await websocket.send_json({"evaluation": [correct,total]})
        await websocket.close()

async def eval2_exec(topic, websocket, run_id):
    total=0
    correct=0
    await download_csv_from_s3(bucket_name="questions-cfa-learning",topic_name=topic)
    csvpath = f'resources/{topic}_setb.csv'
    with open(csvpath, 'r', encoding='utf-8') as file:
            # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        data=[]
        for row in csv_reader:
            question,real_ans = row['Question'], row['Answer']
            # await websocket.send_json({"message": f"question is:\n:{question}"})
            total+=1
            retries = 0
            ans=""
            while retries < 3:
                try:
                    ans = await find_ans_using_knowledge(question)
                    # await websocket.send_json({"message": "done"})
                    break
                except Exception as e:
                    await websocket.send_json({"message": "timed out. waiting for 30 sec"})
                    await asyncio.sleep(10)
                    retries+=1
            await asyncio.sleep(3)
            # await websocket.send_json({"message": f"predicted answer is: \n{ans}"})
            print()
            ans_op = await fetch_option(ans)
            # st.write(ans_op)
            # await websocket.send_json({"message": f"real answer is: \n{real_ans}"})
            real_op = await fetch_option(real_ans)
            # st.write(real_op)
            data.append({
                "question": question,
                "real": real_ans,
                "predicted": ans
            })
            await websocket.send_json({"table": data})
            if ans_op == real_op:
                correct+=1
                # if correct == 1:
                #     break
        await upload_run(websocket,run_id,"knowledge_approach", correct, total, topic)
        await websocket.send_json({"evaluation": [correct,total]})
        await websocket.close()

async def send_evaluatuin_status(websocket,topic,evaluate, run_id, active_connections):
    try:
        # await websocket.send_json({"message": "starting evaluation"+ run_id})
        if topic == 't1':
            topic_req = "Extensions of Multiple Regression"
        elif topic == 't2':
            topic_req = 'Evaluating Regression Model Fit and Interpreting Model Results'
        else:
            topic_req = 'Model Misspecification'
        if evaluate == "methoda":
            await eval1_exec(topic_req, websocket,run_id)               
            if run_id in active_connections:
                    del active_connections[run_id]  # Remove connection from active_connections
            return
        else:
            await eval2_exec(topic_req, websocket,run_id)               
            if run_id in active_connections:
                    del active_connections[run_id]  # Remove connection from active_connections
            return
    except Exception as e:
        print(str(e))
        await websocket.send_json({"message": str(e)})
        