from flask import g, Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os


def create_app(options=None):
    app = Flask(__name__)
    # app.config.from_envvar('APP_SETTINGS')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",None)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # apply any configuration override options
    if options is not None:
      for key, value in options.items():
        app.config[key] = value

    return app

app = create_app()
db = SQLAlchemy(app)

rest_model_mapping = {}


from lumavate_service_util import icon_blueprint, lumavate_blueprint
from routes import *

app.register_blueprint(lumavate_blueprint)
app.register_blueprint(icon_blueprint)



if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")


