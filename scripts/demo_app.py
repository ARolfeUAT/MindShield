"""Demo Flask app for MindShield UI."""

from flask import Flask
from mindshield.ui import ui_blueprint
from config.mock_data import generate_mock_data

app = Flask(__name__)
app.config['MOCK_REQUESTS'] = generate_mock_data()['requests']
app.config['MOCK_LOGS'] = generate_mock_data()['logs']
app.register_blueprint(ui_blueprint, url_prefix='/mindshield')

if __name__ == '__main__':
    app.run(debug=True)
