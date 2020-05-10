from backend import create_app
import os
from backend import api

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
api.init_app(app)

