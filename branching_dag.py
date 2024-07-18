from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

def choose_branch():
    if datetime.now().second % 2 == 0:
        return 'even_task'
    else:
        return 'odd_task'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 18),
    'retries': 1,
}

dag = DAG(
    'branching_dag',
    default_args=default_args,
    description='A simple branching DAG',
    schedule_interval='@daily',
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)

branch = BranchPythonOperator(
    task_id='branch',
    python_callable=choose_branch,
    dag=dag,
)

even_task = DummyOperator(
    task_id='even_task',
    dag=dag,
)

odd_task = DummyOperator(
    task_id='odd_task',
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)

start >> branch >> [even_task, odd_task] >> end
