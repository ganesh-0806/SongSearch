from flask import Blueprint,redirect, render_template, request, url_for, jsonify
from . import db
from . import user

playlist = Blueprint('playlist', __name__)

@playlist.route('/playlist', methods=['GET','POST'])
def dashboard():
    return render_template('playlist.html')

@playlist.route('/playlist/addSong', methods=['POST'])
def addSong():
    if request.method == 'POST':
        # Get the data from the form
        username = user.username
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

@playlist.route('/playlist/deleteSong', methods=['POST'])
def deleteSong():
    if request.method == 'POST':
        # Get the data from the form
        username = user.username
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
        
@playlist.route('/playlist/deleteAll', methods=['POST'])
def deleteAll():
    if request.method == 'POST':
        # Get the data from the form
        username = user.username

        userCollection = db.Userscollection

        userCollection.update_one(
            {'username': username},
            {'$unset': {'SongIDs': {}}},
            upsert=False
        )

        return jsonify({'message': 'Songs Deletion successful'}), 200
    
@playlist.route('/playlist/getSongs', methods=['POST'])
def getSongs():
    if request.method == 'POST':
        # Get the data from the form
        username = user.username

        userCollection = db.Userscollection
        songsCollection = db.Songcollection

        user_document = userCollection.find_one({'username': username})
        song_ids = user_document.get('SongIDs', [])
        songs = songsCollection.find({'SongID': {'$in': song_ids}})
        return list(songs)