import requests
import streamlit as st
import asyncio
import websockets
import zipfile
from trigger_dag import trigger_dag
# Endpoint URLs
GET_DAG_STATUS_URL = "http://fastapi-service:8000/dag_status/"
def get_dag_status(dag_run_id):
    response = requests.get(GET_DAG_STATUS_URL + dag_run_id)
    return response.json()

async def receive_updates(dag_id,dag_run_id):
    uri = f"ws://fastapi-service:8000/ws/{dag_id}/{dag_run_id}"  # Replace with your FastAPI server URL
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            st.write("Received update:", message)
def fetch_updates(dag_id,dag_run_id):
    if dag_run_id:
        st.write(f"Waiting for updates...")
        try:
            asyncio.run(receive_updates(dag_id,dag_run_id))
            st.write(f"Task Completed")
        except asyncio.exceptions.CancelledError:
            print("WebSocket task was cancelled.")
        except Exception as e:
            st.write(f"Task Completed")
def triggerDag(s3_uri,dag_id='question_generate', topic=""):
        if s3_uri:
            st.success("File uploaded successfully!")
            st.write("S3 URI:", s3_uri)
            dag_run_info, rid = trigger_dag(dag_id, s3_uri=s3_uri, topic=topic)
            run_id = rid
            st.write(dag_run_info)
            dag_run_id = run_id
            fetch_updates(dag_id,dag_run_id)
def process_pdf(s3_uri, dag_id, topic=""):
    if s3_uri:
        triggerDag(s3_uri=s3_uri, dag_id=dag_id,topic=topic) 


