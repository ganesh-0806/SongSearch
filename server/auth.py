from flask import Blueprint,redirect, render_template, request, url_for, jsonify
from . import db
from .models import user
from .playlist import dashboard

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def landing():
    return render_template('login.html')

@auth.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # Get the data from the form
        username = request.form['login-username-value']
        password = request.form['login-password-value']

        userCollection = db.Userscollection
        userRecord = userCollection.find_one({'username': username})
        if userRecord is None:
            return jsonify({'message': 'User not found'}), 404
        elif password != userRecord["password"]:
            return jsonify({'message': 'Wrong password'}), 404
        else:
            user.setusername(username)
            user.setpassword(password)
            return redirect(url_for('playlist.dashboard'))
            

@auth.route('/register/', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # Get the data from the form
        username = request.form['register-username-value']
        password = request.form['register-password-value']

        userCollection = db.Userscollection
        userRecord = userCollection.find_one({'username': username})
        if userRecord is None:
            userCollection.insert_one({'username': username, 'password': password, 'SongIDs':[]})
            user.setusername(username)
            user.setpassword(password)
            return redirect(url_for('playlist.dashboard'))
        else:
            return jsonify({'message': 'User already exists'}), 404
        
@auth.route('/logout/', methods=['GET'])
def logout():
    user.setusername(None)
    user.setpassword(None)
    return redirect(url_for('landing'))