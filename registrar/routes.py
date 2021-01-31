from flask import render_template, url_for, flash, redirect, request, abort
from registrar import app

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')