from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

with DAG(dag_id='docker_operator_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    run_docker = DockerOperator(
        task_id='run_docker_container',
        image='ubuntu:latest',
        command='echo "Hello from Docker!"',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )
