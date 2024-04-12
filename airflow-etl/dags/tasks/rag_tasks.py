from helpers.create_knowledge_base import create_technical_note, process_markdown
import os
from helpers.qa_generator import generate_qa

def generate_qa_seta_task_function(**context):
    res_path = os.path.join(os.path.dirname(__file__), 'resources')
    namespace_suffix = "seta"
    topic_name = context['dag_run'].conf['topic_name']
    run_id = context['dag_run'].run_id
    task_instance = context['task_instance']
    data = task_instance.xcom_pull(task_ids='download_file_qa') 
    return generate_qa(run_id, data,namespace_suffix,topic_name)

def generate_qa_setb_task_function(**context):
    res_path = os.path.join(os.path.dirname(__file__), 'resources')
    namespace_suffix = "setb"
    topic_name = context['dag_run'].conf['topic_name']
    run_id = context['dag_run'].run_id
    task_instance = context['task_instance']
    data = task_instance.xcom_pull(task_ids='download_file_qa') 
    return generate_qa(run_id, data,namespace_suffix,topic_name)

def create_technical_note_task_function(**context):
    res_path = os.path.join(os.path.dirname(__file__), 'resources')
    run_id = context['dag_run'].run_id
    task_instance = context['task_instance']
    data = task_instance.xcom_pull(task_ids='download_file_knowledge') 
    return create_technical_note(run_id,data)

def process_markdown_task_function(**context):
    res_path = os.path.join(os.path.dirname(__file__), 'resources')
    run_id = context['dag_run'].run_id
    task_instance = context['task_instance']
    data = task_instance.xcom_pull(task_ids='download_file_knowledge') 
    return process_markdown(run_id,data)