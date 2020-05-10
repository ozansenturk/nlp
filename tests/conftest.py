import pytest
from backend import create_app, api

@pytest.fixture
def app():
    application = create_app('testing')
    api.init_app(application)
    application.app_context().push()
    return application
