from flask import Blueprint,redirect, render_template, request, url_for, jsonify
from . import db
from .models import user

playlist = Blueprint('playlist', __name__)

@playlist.route('/playlist/', methods=['GET','POST'])
def dashboard():
    username = user.getusername()
    if username == None:
        return redirect(url_for('auth.landing'))
    return render_template('playlist.html', username=username)

@playlist.route('/playlist/addSong/', methods=['POST'])
def addSong():
    if request.method == 'POST':
        # Get the data from the form
        username = user.getusername()
        songID = request.form['add-song-value']

        userCollection = db.Userscollection
        songCollection = db.Songcollection

        song = songCollection.find_one({'SongID': songID})
        if song:
            document = userCollection.find_one({'username': username, 'SongIDs': songID})
            if document:
                return jsonify({'message': 'Song already in the playlist'}), 404
            
            userCollection.update_one({'username': username}, {'$push': {'SongIDs': songID}})
        else:
            return jsonify({'message': 'Song not found'}), 404
    return redirect(url_for('playlist.dashboard'))

@playlist.route('/playlist/deleteSong/', methods=['POST'])
def deleteSong():
    if request.method == 'POST':
        # Get the data from the form
        username = user.getusername()
        songID = request.form['delete-song-value']

        userCollection = db.Userscollection
        songCollection = db.Songcollection

        song = songCollection.find_one({'SongID': songID})
        if song:
            document = userCollection.find_one({'username': username, 'SongIDs': songID})
            if document:
                userCollection.update_one({'username': username}, {'$pull': {'SongIDs': songID}})
            else:
                return jsonify({'message': 'Song is not the playlist'}), 404
            
        else:
            return jsonify({'message': 'Song not found'}), 404
    return redirect(url_for('playlist.dashboard'))
        
@playlist.route('/playlist/deleteAll/', methods=['POST'])
def deleteAll():
    if request.method == 'POST':
        # Get the data from the form
        username = user.getusername()

        userCollection = db.Userscollection

        userCollection.update_one(
            {'username': username},
            {'$unset': {'SongIDs': {}}},
            upsert=False
        )

        return jsonify({'message': 'Songs Deletion successful'}), 200
    return redirect(url_for('playlist.dashboard'))
    
@playlist.route('/playlist/getSongs/', methods=['POST'])
def getSongs():
    if request.method == 'POST':
        # Get the data from the form
        username = user.getusername()

        userCollection = db.Userscollection
        songsCollection = db.Songcollection

        user_document = userCollection.find_one({'username': username})
        song_ids = user_document.get('SongIDs', [])
        search_ids = []
        for search in song_ids:
            search_ids.append(search)
        songs = songsCollection.find({'SongID': {'$in': search_ids}})
        res = []
        for song in songs:
            res.append(str(song))
        return res