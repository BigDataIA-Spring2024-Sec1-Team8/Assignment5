import streamlit as st

import websockets
import uuid
import asyncio
import json
import pandas as pd
import matplotlib.pyplot as plt

def eval1_exec(topic):
    try:
        if topic == "Extensions of Multiple Regression":
            topic_req = 't1'
        elif topic == 'Evaluating Regression Model Fit and Interpreting Model Results':
            topic_req = 't2'
        else:
            topic_req = 't3'
        asyncio.run(receive_evaluation_updates(topic=topic_req, method="methoda"))
        st.write(f"Task Completed")
    except asyncio.exceptions.CancelledError:
        print("WebSocket task was cancelled.")
    except Exception as e:
        st.write(f"Task Completed")
   

def eval2_exec(topic):
    try:
        if topic == "Extensions of Multiple Regression":
            topic_req = 't1'
        elif topic == 'Evaluating Regression Model Fit and Interpreting Model Results':
            topic_req = 't2'
        else:
            topic_req = 't3'
        asyncio.run(receive_evaluation_updates(topic=topic_req, method="methodb"))
        st.write(f"Task Completed")
    except asyncio.exceptions.CancelledError:
        print("WebSocket task was cancelled.")
    except Exception as e:
        st.write(f"Task Completed")
def evaluation_result(correct_count,total_questions):
    # correct_count = 25  # Example value
    # total_questions = 50
    incorrect_count = total_questions - correct_count

    # Create a pie chart to visualize correct and incorrect answers
    labels = ['Correct', 'Incorrect']
    sizes = [correct_count, incorrect_count]
    colors = ['#4CAF50', '#FF5733']  # Green for correct, red for incorrect

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Display the pie chart using Streamlit
    st.pyplot(fig)

    # Display text indicating the number of correct questions out of total 50
    st.text(f"Correctly answered {correct_count} out of {total_questions} questions")
async def receive_evaluation_updates(topic, method):
    uuid_string = str(uuid.uuid4())
    uri = f"ws://fastapi-service:8000/ws/{topic}/{method}/{uuid_string}"  # Replace with your FastAPI server URL
    try:
        st.write("starting run "+ uuid_string)
        table_placeholder = st.empty()
        async with websockets.connect(uri) as websocket:
            while True:
                message = await websocket.recv()
                json_message = json.loads(message)
                extracted_message = json_message.get('message', None)
                # st.write("jo")
                if extracted_message:
                    st.write(extracted_message)
                extracted_table = json_message.get('table', None)
                if extracted_table:
                    table_placeholder.table(pd.DataFrame(extracted_table))
                evaluation = json_message.get('evaluation', None)
                if evaluation and len(evaluation)==2:
                    evaluation_result(evaluation[0],evaluation[1])
    except Exception as e:
        st.write(str(e))