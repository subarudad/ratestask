from flask import Flask, Blueprint
import logging

from ratestask.config import Config
from ratestask.api import Api
from ratestask.apis.rates import api as ns1
from ratestask.apis.health import api as ns2


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')


api = Api(
    title="Ratestask API",
    version="0.1",
    description="API for Ratestask",
    doc="/doc",
)

api.add_namespace(ns1, path='/rates')
api.add_namespace(ns2, path='/health')

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.setdefault("RESTX_MASK_SWAGGER", False)
api.init_app(app)

app.logger.warning('{app_name} {app_version} starting in {env}...'.format(
    app_name=Config.APP_NAME,
    app_version=Config.APP_VERSION,
    env=Config.FLASK_ENV
))


@app.before_request
def clear_trailing():
    from flask import redirect, request

    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
