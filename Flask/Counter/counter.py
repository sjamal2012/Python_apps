from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')

def counter():
    session['counter']
    session['counter'] += 1
    return render_template('counter.html')

@app.route('/add2', methods=['POST'])

def add_2():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])

def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
