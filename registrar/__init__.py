from flask import Flask
from os import path, makedirs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bfe24868cd233b3e9be322b976321a0f'
app.config['PHOTOS'] = '/tmp/registrar/photos'

from registrar import routes

dir = app.config['PHOTOS']
makedirs(path.join(dir, 'faces'), exist_ok=True)
