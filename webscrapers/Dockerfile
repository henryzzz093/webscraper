FROM python:3.10-slim-buster as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM builder as dev 

FROM builder as prod
COPY webscrapers . 
