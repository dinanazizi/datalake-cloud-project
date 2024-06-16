import os
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from urllib.request import urlretrieve
import pendulum
from datetime import timedelta
from minio import Minio
from minio.error import S3Error

def download_file(url, file_path):
    try:
        urlretrieve(url, file_path)
        print(f"File downloaded successfully from {url}!")
    except Exception as e:
        print(f"Error downloading file from {url}: {e}")

def upload_to_minio(file_path, file_name, **kwargs):
    # MinIO configuration
    minio_client = Minio(
        'dl-minioserver:9000',  # Use service name as hostname
        access_key='minio-acc-key',
        secret_key='minio-secret-key',
        secure=False
    )
    bucket_name = 'open-data-pendidikan'
    
    # Ensure the bucket exists
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)

    object_name = file_name

    # Upload the file to MinIO
    try:
        minio_client.fput_object(bucket_name, object_name, file_path)
        print(f"File {file_name} uploaded successfully to MinIO!")
    except S3Error as e:
        print(f"Error uploading file {file_name} to MinIO: {e}")

def process_url(url_dict, **kwargs):
    title = url_dict.get('title', 'Untitled')
    url = url_dict.get('url', '')
    
    execution_date = kwargs['execution_date']
    execution_time = execution_date.strftime('%Y%m%dT%H%M%S')
    file_name = f"{title}_{execution_time}.xlsx"
    file_path = os.path.join('/tmp', file_name)  # Save temporarily before uploading

    # Download the file
    download_file(url, file_path)
    
    # Upload the file to MinIO
    upload_to_minio(file_path, file_name, **kwargs)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': pendulum.datetime(2024, 5, 24, 17, 55, 0, tz='Asia/Jakarta'),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'download_files_batch',
    default_args=default_args,
    description='A DAG to download files from URLs and save them to MinIO',
    schedule_interval=timedelta(minutes=5),
)

urls = [
    {"title": "", "url": ""},
    # Add URLs and Title
]

for i, url_dict in enumerate(urls):
    task_id = f'download_and_upload_task_{i}'
    download_and_upload_task = PythonOperator(
        task_id=task_id,
        python_callable=process_url,
        op_kwargs={'url_dict': url_dict},
        provide_context=True,
        dag=dag,
    )

    download_and_upload_task
