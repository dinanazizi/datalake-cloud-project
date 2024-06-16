# datalake-cloud-project

# Architecture
<img width="1127" alt="image" src="https://github.com/dinanazizi/datalake-cloud-project/assets/110298446/2874ded3-9770-427e-b18c-b76ff02d5b8d">


# Tech Stack

Technologies needed to build a *Datalake* ecosystem include:

## Apache Airflow

Apache Airflow is a platform to programmatically author, schedule, and monitor workflows. It is essential for orchestrating data pipelines within the Datalake ecosystem, ensuring that data flows smoothly and efficiently from one stage to the next.

## Dremio

Dremio is an engine required for processing various forms of data, whether it is unstructured, semi-structured, or structured. Dremio is also commonly referred to as a **Data Lake Engine.** One of its advantages is its ability to process unstructured data using *Query Like*.

## Minio Server

Minio Server is a modern object storage system similar to Amazon Web Service (AWS) S3. Minio is used as **Data Lake Storage.**

## Nessie

Nessie is a data versioning system similar to Git versioning.

## Metabase

Metabase is a data analytics platform with capabilities to create graphs, perform data queries, and generate executive summaries.

# STEPS

1. Create folders and move the JAR file:
- https://github.com/Baoqi/metabase-dremio-driver/releases/download/1.3.1/dremio.metabase-driver.jar
2. Create a metabase folder inside the datalake folder.
- Download the dremio.metabase-driver.jar file and move it to the metabase folder.
3. Create a Dockerfile for Metabase:
- Write a Dockerfile inside the metabase folder with the specified content.
4. Set up Apache Airflow:
- Create a dags folder inside the dl-airflow folder.
- Write the Python code for the DAG.
5. Create a Dockerfile for Airflow with the specified content.
6. Write a docker-compose.yml file to set up the entire ecosystem.
7. Create Docker networks:
docker network create external_network
docker network create iceberg_env
8. Run the docker-compose.yml

