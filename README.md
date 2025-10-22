

# Airflow Tutorial Pipeline

Ce dépôt contient un **tutoriel complet pour construire une pipeline de données simple avec Apache Airflow** (version 3.1.0) en utilisant Docker Compose.

Le projet illustre :
- La mise en place d’un environnement Airflow avec Docker,
- La création et exécution d’un DAG qui crée des tables PostgreSQL,
- Le téléchargement d’un fichier CSV depuis internet,
- L’insertion et le nettoyage des données dans une base PostgreSQL,
- La gestion des dépendances entre tâches dans Airflow.

Ce tutoriel est idéal pour les débutants souhaitant se familiariser avec Airflow, comprendre la structuration d’un DAG, et apprendre à automatiser un workflow ETL simple.

---

## Installation et exécution

1. Cloner ce dépôt :

2. Lancer l’environnement Airflow avec Docker Compose :

   
3. Accéder à l’interface Airflow : [http://localhost:8080](http://localhost:8080)

4.  Définir la connexion PostgreSQL dans l’interface Airflow (titre : `tutorial_pg_conn`)

5. Activer et lancer le DAG `process_employees`
