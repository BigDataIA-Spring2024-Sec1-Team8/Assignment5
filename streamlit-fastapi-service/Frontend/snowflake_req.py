import requests


backend_url = "http://fastapi-service:8000"

def fetch_run_res(method, topic):
    # Fetch data from FastAPI backend

    response = requests.get(f"{backend_url}/data", params={"method": method, "topic": topic})
    data = response.json()
    return data