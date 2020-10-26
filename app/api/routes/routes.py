"""
app.api.routes.routes
---------------------

"""


from flask import Blueprint

api = Blueprint('api', __name__)


@api.route("/create_course")
def api_home():
    return "<h1>API Home</h1>"


@api.route("/create_course")
def api_home():
    return "<h1>API Home</h1>"

