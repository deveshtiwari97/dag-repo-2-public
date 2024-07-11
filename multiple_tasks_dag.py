
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def task_1():
    print("Task 1 executed")

def task_2():
    print("Task 2 executed")

def task_3():
    print("Task 3 executed")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

with DAG(dag_id='multiple_tasks_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    t1 = PythonOperator(
        task_id='task_1',
        python_callable=task_1
    )

    t2 = PythonOperator(
        task_id='task_2',
        python_callable=task_2
    )

    t3 = PythonOperator(
        task_id='task_3',
        python_callable=task_3
    )

    t1 >> [t2, t3]
