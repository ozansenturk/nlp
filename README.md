## Modern Flask Application

This project demonstrates scalable python flask restful application for Natural Language Processing. 

It supports:

- Modern Rest APIs
- Swagger (self documentation)
- Postman
- Dockerization
- Docker Compose
- Data Ingestion (Text file)
- Application Factory Pattern
- Gunicorn deploy

Feel free to reach me out if you have additional
questions. ozan.senturk@gmail.com

You can visit url below for swagger Rest API self documentation
http://www.cloudtr.co.uk:5001

You can see more samples in the url below
https://www.analyticai.co.uk


## How to install

```python
python3 -m venv venv
source venv/bin/activate
pip install spacy
python3 -m spacy download en_core_web_sm
pip install -r requirements.txt
python3 nlp.py
```

## Test

```python
python3 $(which py.test)
```

## Postman
You can easily create the postman collection for your APIs with the step below

```python
python3 postman.py
```

## Docker
Build and run your docker container with docker-compose

```python
docker-compose build
docker-compose up
docker ps -a
docker logs [CONTAINERID] -f
```