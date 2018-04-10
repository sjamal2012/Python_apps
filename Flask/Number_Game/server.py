from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'verySecret'

@app.route('/')
def numbers():
    import random
    session['number'] = random.randrange(0,101)

    return render_template('index.html')

@app.route('/process', methods=['POST'])

def guess():

    if int(request.form['guess']) == session['number']:
        correct = session['number']
        session.pop('number')
        import random
        session['number'] = random.randrange(0,101)

        return render_template('index_right.html', correct=str(correct) + ' was the number!', high='', low='')

    elif int(request.form['guess']) > session['number']:

        return render_template('index_wrong.html', wrong="Too high!")

    elif int(request.form['guess']) < session['number']:

        return render_template('index_wrong.html', wrong="Too low!")

app.run(debug=True)
