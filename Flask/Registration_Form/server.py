from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    fnCheck = len(request.form['first_name'])
    lnCheck = len(request.form['last_name'])
    emCheck = len(request.form['email'])
    pwCheck = len(request.form['password'])
    cpCheck = len(request.form['confirm_password'])

    if len(request.form['first_name']) < 1:
        flash("'First name' cannot be empty!")
    if len(request.form['last_name']) < 1:
        flash("'Last name' cannot be empty!")
    if len(request.form['email']) < 1:
        flash("'Email' cannot be empty!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address.")
    if len(request.form['password']) < 1:
        flash("'Password' cannot be empty!")
    elif len(request.form['password']) < 8:
        flash("'Password' must be more than 8 characters!")
    elif request.form['password'] != request.form['confirm_password']:
        flash("Password don't match!")
    else:
        flash("Thanks for submitting your information.")

    return render_template('info.html',
        first_name = first_name,
        last_name = last_name,
        email = email,
        password = password,
        confirm_password = confirm_password,
        fnCheck = fnCheck,
        lnCheck = lnCheck,
        pwCheck = pwCheck,
        emCheck = emCheck,
        cpCheck = cpCheck,
        EMAIL_REGEX = EMAIL_REGEX
        )

app.run(debug=True)
