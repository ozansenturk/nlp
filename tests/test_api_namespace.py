'''
Test the Feature Extraction operations

'''
from unittest.mock import ANY
import http.client
import json
from flask_restx import fields, marshal
from backend import api

from faker import Faker
fake = Faker()

def test_lemmatize(client):
    text_fields = {}

    text_fields['type'] = fields.String(attribute='type')
    text_fields['content'] = fields.String(attribute='content')

    text = {'type': 'lemmatize', 'content': fake.text(240)}

    data_ = json.dumps(marshal(text, text_fields))

    response = client.post('/api/lemmatize/', data= data_,
                           content_type = 'application/json')
    result = response.json

    assert http.client.CREATED == response.status_code

    expected = {
        'type': ANY,
        'content': ANY
    }
    assert result == expected


def test_basic_export(app):

    urlvars = False  # Build query strings in URLs
    swagger = True  # Export Swagger specifications

    app.app_context().push()

    data = api.as_postman(urlvars=urlvars, swagger=swagger)

    assert data["description"] == "Text Analytics"
    assert len(data["requests"]) == 5