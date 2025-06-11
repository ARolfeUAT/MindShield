import pytest
from flask import Flask
from mindshield.ui import ui_blueprint
from config.mock_data import generate_mock_data


@pytest.fixture
def app():
    """Creates a Flask app with MindShield UI Blueprint for testing."""
    flask_app = Flask(__name__)
    flask_app.config['TESTING'] = True
    flask_app.register_blueprint(ui_blueprint, url_prefix='/mindshield')

    # Mock data for testing
    flask_app.config['MOCK_REQUESTS'] = generate_mock_data()['requests']
    flask_app.config['MOCK_LOGS'] = generate_mock_data()['logs']

    return flask_app


@pytest.fixture
def client(app):
    """Provides a test client for the Flask app."""
    return app.test_client()


@pytest.fixture
def mock_requests(app):
    """Provides mock access requests."""
    return app.config['MOCK_REQUESTS']


@pytest.fixture
def mock_logs(app):
    """Provides mock access logs."""
    return app.config['MOCK_LOGS']