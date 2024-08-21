from quart import Blueprint, Response, current_app
from quart.views import MethodView
from .util import class_route

blp = Blueprint("Crash", __name__)

@class_route(blp, "/crash")
class Crash(MethodView):
    init_every_request = False

    async def get(self):
        print(1.0/0.0)

        return Response("pong", status=200, mimetype='text/plain')


@class_route(blp, "/warn")
class Warn(MethodView):
    init_every_request = False

    async def get(self):
        current_app.logger.warning('This is a warning message')

        return Response("warning", status=200, mimetype='text/plain')
