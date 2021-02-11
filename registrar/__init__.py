from flask import Flask
from os import path, makedirs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bfe24868cd233b3e9be322b976321a0f'
app.config['DATA'] = '/tmp/registrar/photos'

from registrar import routes

dir = app.config['DATA']
makedirs(path.join(dir, 'faces'), exist_ok=True)
makedirs(path.join(dir, 'training'), exist_ok=True)
