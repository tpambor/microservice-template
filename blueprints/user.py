from flask import Blueprint, Response, current_app
from flask.views import MethodView
from repositories import UserRepository
from .util import class_route

blp = Blueprint("Users", __name__)

@class_route(blp, "/test/<id>")
class UserView(MethodView):
    init_every_request = False

    def get(self, id):
        user_repository = current_app.repositories[UserRepository]

        print(user_repository.get_user('123'))

        return Response(f"the user {id}", status=200, mimetype='text/plain')
