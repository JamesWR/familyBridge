import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import src.model

# create and configure the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432" #os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
module = model.BridgeModel(db)
migrate = Migrate(app, db)

@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/makegame')
def makeGame():
    module.make_game({'player_1': "j", 'player_2': "c", 'player_3': "l", 'player_4': "a"})