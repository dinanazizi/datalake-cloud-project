# DOCKER FILE AIRFLOW
from apache/airflow:latest

USER root

RUN apt-get update && \
	apt-get -y install git && \
	apt-get -y install python3-pip && \
	pip3 install pendulum && \
	pip3 install minio