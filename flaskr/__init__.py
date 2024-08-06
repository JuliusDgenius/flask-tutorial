import os

from flask import Flask


def create_app(test_config=None):
    # Fubction to create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exits, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the config if passed in
        app.config.from_mapping(test_config)

    # ensure rhe instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # make a simple page that display hello
    @app.route('/hello')
    def hello():
        return 'Hello, world!'

    return app
