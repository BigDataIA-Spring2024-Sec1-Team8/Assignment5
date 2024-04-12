from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import os
from tasks.download_from_s3 import download_from_s3
from tasks.extract_task import extract
# from tasks.extract_task import extract
from tasks.rag_tasks import generate_qa_seta_task_function,generate_qa_setb_task_function, create_technical_note_task_function,process_markdown_task_function 
from tasks.upload_to_s3 import upload_csv_to_s3

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 19),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

knowledge_base_dag = DAG(
    'knowledge_base',
    default_args=default_args,
    description='Download PDF file from S3',
    start_date=datetime(2024, 3, 19),
    schedule_interval=None,
    catchup=False
)
question_generate_dag = DAG(
    'question_generate',
    default_args=default_args,
    description='question_generate_dag',
    start_date=datetime(2024, 3, 19),
    schedule_interval=None,
    catchup=False
)

def remove_files_task(**context):
    dags = os.path.join(os.getcwd(), 'dags')
    res_path = os.path.join(dags, 'resources')
    run_id = context['dag_run'].run_id
    res_path = os.path.join(res_path, str(run_id))

    for filename in os.listdir(res_path):
        file_path = os.path.join(res_path, filename)
        # Check if the path is a file (not a directory)
        if os.path.isfile(file_path):
            # Remove the file
            os.remove(file_path)
    os.rmdir(res_path)
task_download_from_s3 = PythonOperator(
        task_id='download_file_qa',
        python_callable=download_from_s3,
        dag=question_generate_dag
    )

extract_text_from_pdf_task = PythonOperator(
        task_id='extract_context_pdf',
        python_callable=extract,
        dag=question_generate_dag
    )
generate_qa_seta_task = PythonOperator(
        task_id='generate_qa_seta',
        python_callable=generate_qa_seta_task_function,
        dag=question_generate_dag
    )
generate_qa_setb_task = PythonOperator(
        task_id='generate_qa_setb',
        python_callable=generate_qa_setb_task_function,
        dag=question_generate_dag
    )
upload_qa_task = PythonOperator(
        task_id='upload_qa_task',
        python_callable=upload_csv_to_s3,
        dag=question_generate_dag
    )
task_download_from_s3_knowledge = PythonOperator(
        task_id='download_file_knowledge',
        python_callable=download_from_s3,
        dag=knowledge_base_dag
    )
knowledge_create_task = PythonOperator(
        task_id='knowledge_create_task',
        python_callable=create_technical_note_task_function,
        dag=knowledge_base_dag
    )
knowledge_upload_task = PythonOperator(
        task_id='knowledge_upload_to_pyncone',
        python_callable=process_markdown_task_function,
        dag=knowledge_base_dag
    )

task_download_from_s3_knowledge >> knowledge_create_task >> knowledge_upload_task 

[task_download_from_s3, extract_text_from_pdf_task] >> generate_qa_seta_task >> upload_qa_task
[task_download_from_s3, extract_text_from_pdf_task] >> generate_qa_setb_task >> upload_qa_task