from flask import Flask, render_template
from flask_login import LoginManager
from flask_pymongo import PyMongo

import config

# Application Configuration Setup
app = Flask(__name__)
app.secret_key = config.SECRET_KEY
app.config['MONGO_URI'] = config.MONGO_URI
mongo = PyMongo(app, config_prefix='MONGO')


login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def home_page():

    return render_template('index.html',
                           title="Home")


if __name__ == '__main__':
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
