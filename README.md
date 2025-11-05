

# Airflow Tutorial Pipeline

Un tutoriel complet pour construire une pipeline ETL simple avec Apache Airflow 3.1.0 et Docker Compose. Ce projet vous permet de **créer, orchestrer et monitorer un workflow de données** sans complexité inutile.

## À propos

Ce projet illustre les concepts fondamentaux d'Apache Airflow :

- Mise en place d'un environnement Airflow avec Docker Compose
- Création et exécution d'un DAG (Directed Acyclic Graph)
- Gestion des dépendances entre tâches
- Intégration avec PostgreSQL
- Automatisation d'un workflow ETL complet (extraction, transformation, chargement)

Ce tutoriel est idéal pour les débutants souhaitant se familiariser avec Airflow, comprendre la structuration d’un DAG, et apprendre à automatiser un workflow ETL simple.


---
Le DAG `process_employees` exécute les tâches suivantes en séquence :

1. Créer les tables PostgreSQL
2. Télécharger un fichier CSV depuis internet
3. Insérer les données dans la base de données
4. Nettoyer et valider les données

---
## Prérequis

- [Docker](https://docs.docker.com/get-docker/) et Docker Compose (version 2.0+)
- [Git](https://git-scm.com/)
- Minimum 2GB de RAM disponible
- Port 8080 (Airflow) et 5432 (PostgreSQL) disponibles

---
## Installation et exécution

1. Cloner ce dépôt :

2. Lancer l’environnement Airflow avec Docker Compose :

   
3. Accéder à l’interface Airflow : [http://localhost:8080](http://localhost:8080)

4.  Définir la connexion PostgreSQL dans l’interface Airflow (titre : `tutorial_pg_conn`)

5. Activer et lancer le DAG `process_employees`

## Utilisation

### Activer et lancer le DAG

1. Dans l'interface Airflow, allez à l'onglet **DAGs**
2. Localisez le DAG `process_employees`
3. Cliquez sur le **bouton d'activation** (toggle) pour l'activer
4. Cliquez sur **Trigger DAG** pour lancer une exécution manuelle

### Monitorer l'exécution

- **Vue en arborescence** : Visualisez le flux de tâches et leurs dépendances
- **Vue calendrier** : Consultez l'historique des exécutions
- **Logs** : Cliquez sur une tâche pour voir ses logs détaillés

### Résultats

Une fois le DAG terminé, consultez les données dans PostgreSQL

