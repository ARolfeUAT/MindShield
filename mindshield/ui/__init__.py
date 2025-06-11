"""MindShield UI Flask Blueprint."""

from flask import Blueprint

ui_blueprint = Blueprint('ui', __name__, template_folder='templates', static_folder='static')

from . import routes