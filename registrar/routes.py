from flask import render_template, url_for, flash, redirect, request, abort
from registrar import app
from registrar.forms import RegistrationForm
from os import path

@app.route("/", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Create image & process
        pass
    return render_template('register.html', title='Register', form=form)
