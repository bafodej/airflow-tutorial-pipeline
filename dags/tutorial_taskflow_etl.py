import json
import pendulum
from airflow.decorators import dag, task

@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["tutorial", "taskflow"],
)
def tutorial_taskflow_etl():
    """
    ### Pipeline ETL avec TaskFlow API
    Un exemple simple qui montre Extract, Transform, Load
    """
    
    @task()
    def extract():
        """
        #### Extract
        Extrait des données depuis une source (ici simulé avec du JSON)
        """
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
        order_data_dict = json.loads(data_string)
        return order_data_dict
    
    @task(multiple_outputs=True)
    def transform(order_data_dict: dict):
        """
        #### Transform
        Calcule la valeur totale des commandes
        """
        total_order_value = 0
        for value in order_data_dict.values():
            total_order_value += value
        
        return {"total_order_value": total_order_value}
    
    @task()
    def load(total_order_value: float):
        """
        #### Load
        Affiche le résultat (normalement on sauvegarderait en DB)
        """
        print(f"Valeur totale des commandes: {total_order_value:.2f}€")
    
    # Construction du pipeline
    order_data = extract()
    order_summary = transform(order_data)
    load(order_summary["total_order_value"])

# Appel du DAG
tutorial_taskflow_etl()
