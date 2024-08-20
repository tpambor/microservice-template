from quart import Blueprint, Response
from quart.views import MethodView
from .util import class_route

blp = Blueprint("Health Check", __name__)

@class_route(blp, "/ping")
class HealthCheck(MethodView):
    init_every_request = False

    async def get(self):
        return Response("pong", status=200, mimetype='text/plain')
