import types
import copy
import quart
import google.cloud.logging

# Workaround problem until fixed upstream
def _flask_request(name):
    if name == 'request':
        if not quart.request:
            return None
        req = copy.copy(quart.request)
        req.environ = {"SERVER_PROTOCOL": f"HTTP/{quart.request.http_version}"}
        return req
    else:
        raise AttributeError()

google.cloud.logging_v2.handlers._helpers.__dict__['flask'] = types.ModuleType("flask")
google.cloud.logging_v2.handlers._helpers.__dict__['flask'].__getattr__ = _flask_request

def setup_cloud_logging():
    client = google.cloud.logging.Client()
    handler = google.cloud.logging.handlers.StructuredLogHandler()
    google.cloud.logging_v2.handlers.setup_logging(handler)
