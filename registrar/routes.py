from flask import render_template, url_for, flash, redirect, request, abort
from registrar import app

@app.route("/")
def index():
    return render_template('index.html')