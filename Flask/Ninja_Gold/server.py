from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random
app = Flask(__name__)
app.secret_key = 'superSecret'

@app.route('/')

def start():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
    return render_template('index.html', gold = session['gold'], activities=session['activities'])

@app.route('/process_money', methods=['POST'])

def process_money():
    time = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
    building = request.form['building']

    if building == 'farm':
        gold = random.randrange(10, 21)
        session['activities'].append({'activity':"You entered a {} and earned {} gold!".format(building, gold), 'class':'win', 'date':time})
    elif building == 'cave':
        gold = random.randrange(5, 11)
        session['activities'].append({'activity':"You entered a {} and earned {} gold!".format(building, gold), 'class':'win', 'date':time})
    elif building == 'house':
        gold = random.randrange(2, 6)
        session['activities'].append({'activity':"You entered a {} and earned {} gold!".format(building, gold), 'class':'win', 'date':time})
    elif building == 'casino':
        gold = random.randrange(-50, 51)
        if gold >= 0:

            session['activities'].append({'activity':"You entered a {} and earned {} gold!".format(building, gold), 'class':'win', 'date':time})
        elif gold < 0:
            session['activities'].append({'activity':"You entered a {} and lost {} gold...ouch".format(building, gold), 'class':'loss', 'date':time})
    session['gold'] += gold
    return redirect('/')

@app.route('/reset', methods=['POST'])

def reset():
    session['gold'] = 0
    session['activities'] = []
    return redirect('/')
app.run(debug=True)
