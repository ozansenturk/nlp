FROM ubuntu:18.04

RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-virtualenv

# set working directory
RUN mkdir -p /home/nlp
WORKDIR /home/nlp

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt requirements.txt

RUN pip install -U spacy
RUN python3 -m spacy download en_core_web_sm
RUN pip install gunicorn
RUN pip install -r requirements.txt

COPY wsgi.py postman.py boot.sh .flaskenv ./
RUN chmod +x boot.sh wsgi.py postman.py

COPY backend backend
COPY core core
COPY tests tests

ENV FLASK_APP nlp.py

EXPOSE 5001
ENTRYPOINT ["./boot.sh"]

#TODO
#docker composer is necessary
#update docker hub details