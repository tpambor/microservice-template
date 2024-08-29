from flask import Flask
from blueprints import BlueprintHealth, BlueprintCrash
from gcp import setup_cloud_logging

API_PREFIX = "/v1/user"

def create_app():
    setup_cloud_logging()

    app = Flask(__name__)

    app.register_blueprint(BlueprintHealth, url_prefix=API_PREFIX)
    app.register_blueprint(BlueprintCrash, url_prefix=API_PREFIX)

    return app
