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
questions


## How to install

python3 -m venv venv
source venv/bin/activate
pip install spacy
python3 -m spacy download en_core_web_sm
pip install -r requirements.txt
python3 nlp.py

## Test
python3 $(which py.test)
