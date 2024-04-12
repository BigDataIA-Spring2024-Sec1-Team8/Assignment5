from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
import requests
import logging
from snowflake_wrapper import *
from dag_status import send_dag_status
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()
from rag.rag_helper_functions import send_evaluatuin_status
AIRFLOW_API_BASE_URL = "http://host.docker.internal:8080/api/v1"
# AIRFLOW_API_BASE_URL = "http://test-airflow-1269873075.us-east-2.elb.amazonaws.com/api/v1"

# Now you have the path to the config file in the `config_path` variable
@app.post("/trigger_dag/{dag_id}")
async def trigger_dag(dag_id: str, dag_run_body: dict):
    try:
        AUTHORIZATION_HEADER = "Basic YWlyZmxvdzphaXJmbG93"

        response = requests.post(
            f"{AIRFLOW_API_BASE_URL}/dags/{dag_id}/dagRuns", 
            headers={
                "Authorization": AUTHORIZATION_HEADER,
                "Content-Type": 'application/json'
                },
            json=dag_run_body
            )
        print(dag_run_body, dag_id)
        response.raise_for_status()  # Raise an exception if the request was not successful
        
        # Extract the DAG run ID from the response
        res=response.json()
        dag_run_id = res["dag_run_id"]
        execution_date = res['execution_date']
        return {"message": f"DAG {dag_id} triggered successfully", "dag_run_id": dag_run_id, "execution_date": execution_date}
    except Exception as e:
        logger.error(f"Failed to trigger DAG {dag_id}: {str(e)}")

        raise HTTPException(status_code=500, detail=f"Failed to trigger DAG {dag_id}: {str(e)}")

active_connections = {}

evaluation_requests = {}
@app.websocket("/ws/{dag_id}/{dag_run_id}")
async def websocket_endpoint(websocket: WebSocket,dag_id:str, dag_run_id: str):
    await websocket.accept()
    active_connections[dag_run_id] = websocket  # Store WebSocket connection
    try:
        await send_dag_status(websocket,dag_id, dag_run_id, active_connections)
    except WebSocketDisconnect:
        pass  # WebSocket disconnected
    finally:
        if dag_run_id in active_connections:
            del active_connections[dag_run_id]

@app.websocket("/ws/{topic}/{evaluate}/{run_id}")
async def websocket_endpoint(websocket: WebSocket,topic:str, evaluate:str, run_id: str):
    await websocket.accept()
    websocket.ping_interval = 60
    evaluation_requests[run_id] = websocket  # Store WebSocket connection
    try:
        # await websocket.send_json({"message": "hello"})
        await send_evaluatuin_status(websocket,topic,evaluate, run_id, evaluation_requests)
    except WebSocketDisconnect:
        pass  # WebSocket disconnected
    finally:
        if run_id in active_connections:
            del evaluation_requests[run_id]

@app.get("/data")
async def fetch_data(method: str = None, topic: str = None) -> List[dict]:
    data=[]
    try:
        data = get_data(method,topic)
    except Exception as e:
        logger.error(str(e))
    return data
