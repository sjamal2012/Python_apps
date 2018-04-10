from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
mysql = MySQLConnector(app,'friendsdb')
app.secret_key = 'secret_key_001'

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=['POST'])
def create():
    if len(str(request.form['first_name'])) < 1 or len(str(request.form['last_name'])) < 1 or len(str(request.form['email'])) < 1:
        flash("All fields must be filled out!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!")
        return redirect('/')
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"

    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_id>/edit')
def edit(friend_id):
    query = "SELECT * FROM friends WHERE id = :friend_id"

    data = {'friend_id': friend_id}

    friends = mysql.query_db(query, data)[0]
    return render_template('edit.html', one_friend=friends)
#
# @app.route('/friends/<friend_id>', methods=['POST'])
# def update(friend_id):
#     query = "UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email WHERE id = :friend_id"
#
#     data = {
#              'first_name': request.form['first_name'],
#              'last_name':  request.form['last_name'],
#              'email': request.form['email'],
#              'friend_id': friend_id
#            }
#
#     mysql.query_db(query, data)
#
#     return redirect('/')
#
# @app.route('/friends/<friend_id>/delete')
# def destroy(friend_id):
#
#     query = "DELETE FROM friends WHERE id = :friend_id"
#
#     data = {
#              'friend_id': friend_id
#            }
#
#     mysql.query_db(query, data)
#     return redirect('/')

app.run(debug=True)
