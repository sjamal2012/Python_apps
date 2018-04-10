from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])

def result():
    name = request.form['name']
    loc = request.form['location']
    lang = request.form['language']
    comment = request.form['comment']

    return render_template('info.html', name = name, loc = loc, lang = lang, comment = comment)

app.run(debug=True)
