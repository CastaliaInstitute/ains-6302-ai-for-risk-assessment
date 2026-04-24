# Anubis autograde image for AINS6302 Module 2
FROM registry.digitalocean.com/anubis/assignment-base-python:latest

RUN pip install --no-cache-dir \
    numpy pandas scikit-learn networkx jupyter nbconvert ipykernel

COPY . /assignment
WORKDIR /assignment
