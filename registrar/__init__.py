from flask import Flask
from os import path, makedirs
from flask_cors import CORS
import os
import csv

app = Flask(__name__)
CORS(app)
app.config['DATA'] = os.path.join('C:\\', 'users', 'stoff', 'projects', 'registrar', 'data')
app.config['OPENCV'] = os.path.join('C:\\', 'users', 'stoff', 'projects', 'registrar', 'opencv')

members = {}

from registrar import routes, helpers
helpers._readMembers()
data = app.config['DATA']
makedirs(data, exist_ok=True)
makedirs(path.join(data, 'faces'), exist_ok=True)
makedirs(path.join(data, 'training'), exist_ok=True)
makedirs(path.join(data, 'members'), exist_ok=True)

