from quart import Quart
from blueprints import BlueprintHealth

API_PREFIX = "/v1/user"

def create_app():
    app = Quart(__name__)

    app.register_blueprint(BlueprintHealth, url_prefix=API_PREFIX)

    return app
