from flask import render_template, url_for, flash, redirect, request, abort
from registrar import app
from registrar.forms import RegistrationForm
from os import path
import registrar.api

@app.route("/", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        photo = form.photo.data.split(',')[1]
        registrar.api.identifyMember(photo)
    return render_template('register.html', title='Register', form=form)
