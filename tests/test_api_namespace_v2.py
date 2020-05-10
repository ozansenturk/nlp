import unittest
from backend import create_app, api
import json
from faker import Faker
from flask_restx import fields, marshal
import io

fake = Faker()

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        api.init_app(self.app)

        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_lemmatize_page(self):

        text_fields = {}

        text_fields['type'] =  fields.String(attribute='type')
        text_fields['content'] = fields.String(attribute='content')

        text = {'type':'lemmatize', 'content':fake.text(240)}

        data_ = json.dumps(marshal(text, text_fields))

        # temp_json = json.loads(temp_str)
        response = self.client.post('/api/lemmatize/',
                                    data=data_, content_type = 'application/json')


        self.assertEqual(201, response.status_code )


    def test_extract_entities(self):

        text_fields = {}

        text_fields['type'] =  fields.String(attribute='type')
        text_fields['content'] = fields.String(attribute='content')

        text = {'type':'lemmatize', 'content':'amazon co. can pusblish government related factories and microsoft doesnt now how to cope with facebook and bill gates is old but elon musk is young'}

        data_ = json.dumps(marshal(text, text_fields))

        # temp_json = json.loads(temp_str)
        response = self.client.post('/api/entities/',
                                    data=data_, content_type = 'application/json')


        self.assertEqual(201, response.status_code )

    def test_upload(self):

        text_file = {'type': '123456'}
        text_file['one_file'] = (io.BytesIO(str.encode(fake.text(240))), 'abc.txt')

        response = self.client.post(
            '/api/upload/', data=text_file, follow_redirects=True,
            content_type='multipart/form-data'
        )
        self.assertEqual(201, response.status_code )