from fastapi import FastAPI
from typing import List
import snowflake.connector
import os
from config_parser import fetch_config
app = FastAPI()

config_path = os.environ.get("CONFIG_PATH")

config = fetch_config(config_path)

snowflake_config = {
    'user': config['snowflake']['SNOWFLAKE_USER'],
    'password': config['snowflake']['SNOWFLAKE_PASSWORD'],
    'account': config['snowflake']['SNOWFLAKE_ACCOUNT'],
    'warehouse': config['snowflake']['SNOWFLAKE_WAREHOUSE'],
    'database': 'CFAInstitute',
    'schema': config['snowflake']['SNOWFLAKE_SCHEMA']
}
async def create_runs_table_if_not_exists(websocket,conn):
    try:
        cur = conn.cursor()
        cur.execute("use schema public")
        # Create table if not exists
        cur.execute("""
        CREATE TABLE IF NOT EXISTS eval_requests (
            run_id VARCHAR(50),
            method VARCHAR(50),
            correct_ans INT,
            total_ques INT,
            topic VARCHAR(225)
        )
        """)
        # await websocket.send_json({"message": "sstaty"})
        cur.close()
    except Exception as e:
        await websocket.send_json({"message": str(e)})


async def insert_record(websocket,conn, run_id,method, correct_ans, total_ques, topic):
    cur = conn.cursor()
    # await websocket.send_json({"message": "statyss"})
    await create_runs_table_if_not_exists(websocket,conn)
    try:
        # Insert record
        cur.execute("""
        INSERT INTO eval_requests (run_id,method, correct_ans, total_ques,topic)
        VALUES (%s, %s, %s, %s,%s)
        """, (run_id,method, correct_ans, total_ques,topic))

        conn.commit()
        cur.close()
        await websocket.send_json({"message": "log completed"})
    except Exception as e:
        await websocket.send_json({"message": str(e)})

async def upload_run(websocket, run_id,method, correct_ans, total_ques,topic):
    conn = snowflake.connector.connect(**snowflake_config)
    # await websocket.send_json({"message": "staty"})
    await insert_record(websocket,conn, run_id,method, correct_ans, total_ques,topic)

def get_data(method, topic) -> List[dict]:    
    
    conn = snowflake.connector.connect(**snowflake_config)
    cursor = conn.cursor()
    if method and method != "all" and topic and topic != "all":
        cursor.execute(f"SELECT run_id, correct_ans, total_ques, method, topic FROM eval_requests WHERE method ILIKE '%{method}%' AND topic ILIKE '%{topic}%'")
    elif method and method != "all":
        cursor.execute(f"SELECT run_id, correct_ans, total_ques, method, topic FROM eval_requests WHERE method ILIKE '%{method}%'")
    elif topic and topic != "all":
        cursor.execute(f"SELECT run_id, correct_ans, total_ques, method, topic FROM eval_requests WHERE topic ILIKE '%{topic}%'")
    else:
        cursor.execute("SELECT run_id, correct_ans, total_ques, method, topic FROM eval_requests")

    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"run": row[0], 
               "topic": row[4],
               "technique": row[3],
               "correct_ans": row[1], 
                "total": row[2],
               } for row in data]

# def get_meta_data() -> List[dict]:
#     conn = snowflake.connector.connect(**snowflake_config)
#     cursor = conn.cursor()
#     cursor.execute("SELECT PDF_NAME, ABSTRACT, title FROM METADATA")
#     data = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return [{"PDF_NAME": row[0],"title": row[2], "abstract": row[1]} for row in data]