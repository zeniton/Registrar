from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bfe24868cd233b3e9be322b976321a0f'

from registrar import routes
