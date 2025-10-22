from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# Fonction Python exemple
def print_hello():
    print("Hello from Airflow!")
    return "Success"

# Définition du DAG
default_args = {
    'owner': 'bafode',
    'depends_on_past': False,
    'start_date': datetime(2025, 10, 22),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'my_first_dag',
    default_args=default_args,
    description='Mon premier DAG Airflow',
    schedule=timedelta(days=1),  # CHANGÉ: schedule au lieu de schedule_interval
    catchup=False,
    tags=['tutorial', 'example'],
) as dag:

    # Tâche 1: Commande Bash
    task1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    # Tâche 2: Fonction Python
    task2 = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello,
    )

    # Tâche 3: Autre commande Bash
    task3 = BashOperator(
        task_id='print_end',
        bash_command='echo "DAG completed!"',
    )

    # Définir l'ordre des tâches
    task1 >> task2 >> task3
