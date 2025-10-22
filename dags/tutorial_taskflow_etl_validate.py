import json
import pendulum
from airflow.decorators import dag, task

@dag(
    schedule=None,
    start_date=pendulum.datetime(2025, 10, 20, tz="UTC"),
    catchup=False,
    tags=["tutorial", "taskflow", "validation"],
)
def tutorial_taskflow_etl_validate():
    """
    ### Pipeline ETL avec validation
    Extract -> Validate -> Transform -> Load
    """
    
    @task()
    def extract():
        """Extrait les données"""
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
        order_data_dict = json.loads(data_string)
        return order_data_dict
    
    @task()
    def validate(order_data_dict: dict):
        """
        #### Validate
        Verifie que les donnees sont valides
        """
        if not order_data_dict:
            raise ValueError("Aucune donnee trouvee!")
        
        # Verifie que toutes les valeurs sont positives
        for order_id, amount in order_data_dict.items():
            if amount <= 0:
                raise ValueError(f"Montant invalide pour commande {order_id}: {amount}")
        
        print(f"Validation OK : {len(order_data_dict)} commandes trouvees")
        return order_data_dict
    
    @task(multiple_outputs=True)
    def transform(order_data_dict: dict):
        """Calcule les statistiques"""
        total_order_value = sum(order_data_dict.values())
        avg_order_value = total_order_value / len(order_data_dict)
        max_order_value = max(order_data_dict.values())
        
        return {
            "total_order_value": total_order_value,
            "avg_order_value": avg_order_value,
            "max_order_value": max_order_value,
            "order_count": len(order_data_dict)
        }
    
    @task()
    def load(stats: dict):
        """Affiche les resultats"""
        print("=" * 50)
        print("STATISTIQUES DES COMMANDES")
        print("=" * 50)
        print(f"Nombre de commandes: {stats['order_count']}")
        print(f"Total des commandes: {stats['total_order_value']:.2f} EUR")
        print(f"Moyenne par commande: {stats['avg_order_value']:.2f} EUR")
        print(f"Commande maximale: {stats['max_order_value']:.2f} EUR")
        print("=" * 50)
    
    # Construction du pipeline
    order_data = extract()
    validated_data = validate(order_data)
    order_summary = transform(validated_data)
    load(order_summary)

# Appel du DAG
tutorial_taskflow_etl_validate()
