from backend import create_app
from dotenv import load_dotenv
import os
from backend import api

import logging
logger = logging.getLogger(__name__)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

application = create_app(os.getenv('FLASK_CONFIG') or 'default')
api.init_app(application)

application.run()