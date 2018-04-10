from flask import Flask, render_template, redirect, request
app = Flask(__name__)

leonardo = "http://res.cloudinary.com/lebspec/image/upload/v1510635908/leonardo_wwrsuz.jpg"
michelangelo = "http://res.cloudinary.com/lebspec/image/upload/v1510635910/michelangelo_rjf476.jpg"
raphael = "http://res.cloudinary.com/lebspec/image/upload/v1510635913/raphael_ymuw3i.jpg"
donatello = "http://res.cloudinary.com/lebspec/image/upload/v1510635892/donatello_nz3dfi.jpg"
megan = "http://res.cloudinary.com/lebspec/image/upload/v1510635911/notapril_zz6yl5.jpg"

@app.route('/')
def init():
    i = 0
    return render_template('index.html', i = i)

@app.route('/ninja')
def all_ninjas():
    i = 1

    return render_template('index.html', i = i, leonardo = leonardo, michelangelo = michelangelo, raphael = raphael, donatello = donatello)

@app.route('/ninja/<color>')
def ninja(color):
    i = 2

    if color == 'blue':
        return render_template('index.html', color = color, leonardo = leonardo)
    if color == 'orange':
        return render_template('index.html', color = color, michelangelo = michelangelo)
    if color == 'red':
        return render_template('index.html', color = color, raphael = raphael)
    if color == 'purple':
        return render_template('index.html', color = color, donatello = donatello)
    else:
        i = 3
        return render_template('index.html', i = i, megan = megan)

app.run(debug=True)
