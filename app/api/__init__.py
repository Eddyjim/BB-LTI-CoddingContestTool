"""
api/__init__.py
-------------------------------------------------------------------
"""
from api import routes, resources
from flask_restful import Api


def init_app(app):
    """

    :param app:
    :return:
    """

    routes.init_app(app)
    resources.init_app(app)
