from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    check = len(request.form['name'])
    check2 = len(request.form['comment'])
    comcheck = len(request.form['comment'])
    if len(request.form['name']) < 1:
        flash("'Name' cannot be empty!")
    if len(request.form['comment']) < 1:
        flash("'Comment' cannot be empty!")
    elif len(request.form['comment']) > 120:
        flash("'Comment' must be less than 120 characters!")
    else:
        flash("Success! Your name is {}".format(request.form['name']))
    name = request.form['name']
    loc = request.form['location']
    lang = request.form['language']
    comment = request.form['comment']

    return render_template('info.html', name = name, loc = loc, lang = lang, comment = comment, check = check, check2 = check2, comcheck = comcheck)

app.run(debug=True)
