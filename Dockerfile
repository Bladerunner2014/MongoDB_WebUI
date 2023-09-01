FROM python:3.11-slim-buster

WORKDIR /infra



# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .


