"""
api/resources/__init__.py
-------------------------------------------------------------------
"""
from flask_restful import Api

from api.resources import Grading


def init_app(app):
    """

    :param app:
    :return:
    """

    api = Api(app)
    api.add_resource(Grading.GradeContest, "/grading/grade_contest/")
