from flask_restx import Api
from flask import Flask
from .api_namespace import api_ns

api = Api(version='0.1', title='Text Feature Extraction Backend API',
          description='Text Analytics')
api.add_namespace(api_ns)

def create_app(config_name):

    from core.config import config
    from werkzeug.middleware.proxy_fix import ProxyFix

    application = Flask(__name__)
    application.config.from_object(config[config_name])
    config[config_name].init_app(application)
    application.wsgi_app = ProxyFix(application.wsgi_app)

    return application
