from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow_yjg',
    'depends_on_past': False,
    'start_date': datetime.utcnow(),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'dumm_test', default_args=default_args, schedule_interval=timedelta(minutes=1))


start = DummyOperator(task_id='start', dag=dag)
mid = DummyOperator(task_id='mid', dag=dag)

end = DummyOperator(task_id='end', dag=dag)

start >> mid >> end
