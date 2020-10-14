import os
from flask import Flask

    # create and configure the app
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'
