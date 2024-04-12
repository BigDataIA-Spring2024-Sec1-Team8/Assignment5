import boto3
import os
def upload_csv_to_s3_func(csv_file_path, bucket_name, object_name):
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY')
    aws_secret_access_key =  os.getenv('AWS_SECRET_KEY')
    s3 = boto3.client('s3', 
                      aws_access_key_id=aws_access_key_id, 
                      aws_secret_access_key=aws_secret_access_key)
    try:
        s3.upload_file(csv_file_path, bucket_name, object_name)
        print(f"File uploaded successfully to bucket '{bucket_name}' as '{object_name}'")
    except Exception as e:
        print(f"Error uploading file: {e}")

def upload_csv_to_s3(**context):
    dags = os.path.join(os.getcwd(), 'dags')
    local_path = os.path.join(dags, 'resources')
    task_instance = context['task_instance']
    
    seta = task_instance.xcom_pull(task_ids='generate_qa_seta')
    setb = task_instance.xcom_pull(task_ids='generate_qa_setb')

    seta_path = os.path.join(local_path, seta)
    setb_path = os.path.join(local_path, setb)
    bucket_name = 'questions-cfa-learning'

    upload_csv_to_s3_func(seta_path, bucket_name, seta)
    upload_csv_to_s3_func(setb_path, bucket_name, setb)
