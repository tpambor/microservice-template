from flask import Blueprint, Response, current_app
from flask.views import MethodView
from .util import class_route

blp = Blueprint("Crash", __name__)

@class_route(blp, "/crash")
class Crash(MethodView):
    init_every_request = False

    def get(self):
        print(1.0/0.0)

        return Response("pong", status=200, mimetype='text/plain')


@class_route(blp, "/warn")
class Warn(MethodView):
    init_every_request = False

    def get(self):
        current_app.logger.warning('This is a warning message')

        return Response("warning", status=200, mimetype='text/plain')
