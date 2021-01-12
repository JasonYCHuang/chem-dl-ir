import os

from flask import Flask

import chem_ir.lib.nn_ir.load_model_data as lmd


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        IP_WHITE_LIST='',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.ir_model = lmd.ir_model()
    app.fg_infers = lmd.fg_infers()

    @app.route('/ping')
    def ping():
        return 'pong'


    from chem_ir.controller.api import ctrl
    app.register_blueprint(ctrl)


    return app
