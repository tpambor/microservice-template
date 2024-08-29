import os
from flask import Flask
from blueprints import BlueprintHealth, BlueprintCrash, BlueprintUser
from repositories import UserRepository
from repositories.firestore import FirestoreUserRepository
from gcp import setup_cloud_logging

API_PREFIX = "/v1/user"

def create_app():
    if os.getenv('ENABLE_CLOUD_LOGGING') == '1':
        setup_cloud_logging()

    app = Flask(__name__)

    app.repositories = {UserRepository: FirestoreUserRepository()}

    app.register_blueprint(BlueprintHealth, url_prefix=API_PREFIX)
    app.register_blueprint(BlueprintCrash, url_prefix=API_PREFIX)
    app.register_blueprint(BlueprintUser, url_prefix=API_PREFIX)

    return app
