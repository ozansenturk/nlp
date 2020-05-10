from flask import json
from backend import api, create_app

import logging
# configure root logger
logging.basicConfig(level=logging.DEBUG)

application = create_app('testing')
api.init_app(application)
application.app_context().push()

urlvars = False  # Build query strings in URLs
swagger = True  # Export Swagger specifications
data = api.as_postman(urlvars=urlvars, swagger=swagger)

application.logger.debug('postman collection {}'.format(json.dumps(data, indent = 4)))
# print('postman collection {}'.format(json.dumps(data, indent = 4)))