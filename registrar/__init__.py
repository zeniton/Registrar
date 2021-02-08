from flask import Flask
from os import path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bfe24868cd233b3e9be322b976321a0f'
app.config['PHOTOS'] = path.join('C:\\', 'Users', 'stoff', 'projects', 'Registrar', 'registrar', 'static', 'photos')

from registrar import routes
