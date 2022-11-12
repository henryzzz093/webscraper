FROM python:3.10-slim-buster
WORKDIR /backend
RUN apt-get update && apt-get install make
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
RUN apt-get install -y default-mysql-client
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["bash", "entrypoint.sh"]