from flask import Flask
from os import path, makedirs
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['DATA'] = '/home/cava/projects/registrar/photos'

from registrar import routes

data = app.config['DATA']
makedirs(data, exist_ok=True)
makedirs(path.join(data, 'faces'), exist_ok=True)
makedirs(path.join(data, 'training'), exist_ok=True)
