from flask import Blueprint, render_template, request, redirect, url_for
from . import db
import json
from .models import user

views = Blueprint('views', __name__)

#Reference: https://miro.medium.com/v2/resize:fit:1550/1*ZlUm8r0NT75-NdTLUveLVQ.png

# Pseudo template
@views.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        abc = True
    response = '{response : 200}'

    username = user.getusername()
    if username == None:
        return redirect(url_for('auth.landing'))
    return render_template('home.html')
    #return '<h1>hello</h1>'

@views.route('/readbyartist/', methods=['GET', 'POST'])
def read_by_artist():
    print('read called artist')
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        song_artist = request.form['view-value-artist']
        if not song_artist:
            return
        collection = db.Songcollection
        result = []
        for val in collection.find({"ArtistName": song_artist}):
            result.append(str(val))

        return result

    response = '{response : 200}'

@views.route('/readbyname/', methods=['GET', 'POST'])
def read_by_name():
    print('read called name')
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        song_name = request.form['view-value-name']
        if not song_name:
            return
        collection = db.Songcollection
        result = []
        for val in collection.find({"Title": song_name}):
            result.append(str(val))

        return result

    response = '{response : 200}'

@views.route('/readbylocation/', methods=['GET', 'POST'])
def read_by_artist_location():
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        artist_location = request.form['view-value-location']
        if not artist_location:
            return
        collection = db.Songcollection
        regex = '.*' + artist_location + '.*'
        result = []
        for val in collection.find({"ArtistLocation": {'$regex': regex}}):
            result.append(str(val))

        return result

    response = '{response : 200}'


@views.route('/readbyyear/', methods=['GET', 'POST'])
def read_by_year():
    print('read called year')
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        song_year = request.form['view-value-year']
        if not song_year:
            return
        collection = db.Songcollection
        result = []
        for val in collection.find({"Year": int(song_year)}):
            result.append(str(val))

        return result

    response = '{response : 200}'

@views.route('/readbyyearrange/', methods=['GET', 'POST'])
def read_by_year_range():
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        song_year_from = request.form['view-value-year-from']
        song_year_to = request.form['view-value-year-to']
        if not song_year_from or not song_year_to:
            return
        collection = db.Songcollection
        result = []
        for val in collection.find({"Year": {'$gte': int(song_year_from), '$lte': int(song_year_to)}}):
            result.append(str(val))

        return result

    response = '{response : 200}'



@views.route('/readbydance/', methods=['GET', 'POST'])
def read_by_danceability():
    print('read called dance')
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        song_dance = request.form['view-value-dance']
        if not song_dance:
            return
        collection = db.Songcollection
        result = []
        for val in collection.find({"Danceability": float(song_dance)}):
            result.append(str(val))

        return result

    response = '{response : 200}'


@views.route('/create/', methods=['GET', 'POST'])
def create():
    print('create called')
    if request.method == 'POST':
        #Interact with db and get details
        create_txt = request.form['create-value']
        print(create_txt)
        if not create_txt:
            return
        collection = db.Songcollection
        collection.insert_one({create_txt})
        result = []
        for val in collection.find():
            result.append(str(val))

        return result
        # jsonify the response

    response = '{response : 200}'


@views.route('/update/', methods=['GET', 'POST'])
def update():
    print('update called')
    if request.method == 'POST':
        #Interact with db and get details
        upd_id = str(request.form['update-id-value'])
        upd_name = str(request.form['update-song-name-value'])
        upd_art = str(request.form['update-song-artist-value'])
        upd_year = int(request.form['update-song-year-value'])
        upd_dance = float(request.form['update-song-dance-value'])
        if not upd_id or not upd_name or not upd_art or not upd_year or not upd_dance:
            return

        collection = db.Songcollection
        if upd_name:
            collection.update_one({"SongID": upd_id}, {"$set": {"Title" : upd_name}})
        if upd_art:
            collection.update_one({"SongID": upd_id}, {"$set": {"ArtistName": upd_art}})
        if upd_year:
            collection.update_one({"SongID": upd_id}, {"$set": {"Year": upd_year}})
        if upd_dance:
            collection.update_one({"SongID": upd_id}, {"$set": {"Danceability": upd_dance}})
        return redirect(url_for('views.home'))
    response = '{response : 200}'

@views.route('/delete/', methods=['GET', 'POST'])
def delete():
    print("delete called")
    if request.method == 'POST':
        del_id = request.form['delete-value']
        #Interact with db and get details
        # jsonify the response
        if not del_id:
            return
        collection = db.Songcollection
        collection.delete_one({"SongID": del_id})
        result = []
        for val in collection.find():
            result.append(str(val))

        return result

    response = '{response : 200}'
