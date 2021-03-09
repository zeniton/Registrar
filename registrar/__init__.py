from flask import Flask
from os import path, makedirs
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config['DATA'] = os.path.join('C:\\', 'users', 'stoff', 'projects', 'registrar', 'data')

from registrar import routes

data = app.config['DATA']
print(data)
makedirs(data, exist_ok=True)
makedirs(path.join(data, 'faces'), exist_ok=True)
makedirs(path.join(data, 'training'), exist_ok=True)
