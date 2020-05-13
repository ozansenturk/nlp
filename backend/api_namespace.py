from flask_restx import Namespace, Resource, fields
from core.utils import lemmatize, pos_tag, extract_ent, read_txt_file
import http.client
from werkzeug.datastructures import FileStorage
import os
from flask import current_app

api_ns = Namespace('api', description='Text analytics related operations')

text_model = api_ns.model('data', {
    'type': fields.String(required=True, description='The type of feature'),
    'content': fields.String(required=True, description='The content of text')
})


@api_ns.route('/lemmatize/')
class Lemmatize(Resource):

    @api_ns.doc('lemmatize text')
    @api_ns.expect(text_model)
    @api_ns.marshal_with(text_model, code=http.client.CREATED)
    def post(self):
        '''Lemmatize the text by removing unnecessary parts'''
        data = api_ns.payload

        before_content = data['content']
        content = lemmatize(before_content)

        temp_dic = {'type':'lemmatize','content': content}

        result = api_ns.marshal(temp_dic, text_model)

        return result, http.client.CREATED



@api_ns.route('/nouns/')
class PosTag(Resource):

    @api_ns.doc('Part of speech tag')
    @api_ns.expect(text_model)
    @api_ns.marshal_with(text_model, code=http.client.CREATED)
    def post(self):
        '''Extracting part of speech tags'''
        data = api_ns.payload

        before_content = data['content']
        content = pos_tag(before_content)

        temp_dic = {'type':'nouns','content': content}

        result = api_ns.marshal(temp_dic, text_model)

        return result, http.client.CREATED


@api_ns.route('/entities/')
class Entities(Resource):

    @api_ns.doc('Extract entities')
    @api_ns.expect(text_model)
    @api_ns.marshal_with(text_model, code=http.client.CREATED)
    def post(self):
        '''Extracting entities'''
        data = api_ns.payload

        before_content = data['content']
        content = extract_ent(before_content)

        temp_dic = {'type':'entities','content': content}

        result = api_ns.marshal(temp_dic, text_model)

        return result, http.client.CREATED


upload_parser = api_ns.parser()
upload_parser.add_argument('type', type=str, required=True)
upload_parser.add_argument('one_file', location='files',
                           type=FileStorage, required=True)


@api_ns.route('/upload/')
@api_ns.expect(upload_parser)
class Upload(Resource):

    @api_ns.doc('Upload text documents')
    @api_ns.marshal_with(text_model, code=http.client.CREATED)
    def post(self):

        args = upload_parser.parse_args()

        type = args['type']
        # if 'file' not in args.files:
        uploaded_file = args['one_file']

        uploaded_file.save(os.path.join(current_app.config['UPLOAD_TXT_FOLDER'], uploaded_file.filename))

        file_content = read_txt_file(uploaded_file.filename)
        flat_content = ''.join(file_content)

        if type == 'lemmatize':
            content = lemmatize(flat_content)
        elif type == 'pos_tag':
            content = pos_tag(flat_content)
        else:
            content = extract_ent(flat_content)

        temp_dic = {'type': 'entities', 'content': content}

        result = api_ns.marshal(temp_dic, text_model)

        return result, http.client.CREATED



# /bin/sh $BUILD_DIR/wait-for.sh -t 240 localhost:5000 -- curl -X POST \
#   http://localhost:5000/v1/sufi_face_match \
#   -H 'Cache-Control: no-cache' \
#   -H 'Postman-Token: 3c1b66e7-bdd4-4707-830c-e2b141088841' \
#   -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
#   -F image=@$BUILD_DIR/test-image.jpg \
#   -F image2=@$BUILD_DIR/test-image.jpg \
#   -F XcallID=CURL &

# {
#     "face_rect": false,
#     "flag1": 0,
#     "flag2": 0,
#     "score": 1
# }