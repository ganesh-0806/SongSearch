from flask import Blueprint, render_template, request, flash, jsonify
from . import db
import json

views = Blueprint('views', __name__)

#Reference: https://miro.medium.com/v2/resize:fit:1550/1*ZlUm8r0NT75-NdTLUveLVQ.png

# Pseudo template
@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        abc = True

    response = '{response : 200}'

    return render_template('home.html')
    #return '<h1>hello</h1>'

@views.route('/read-hardcoded', methods=['GET', 'POST'])
def read_hardcoded():
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        abc = True

    response = '{response : 200}'
    collection = db.Songcollection
    result = []
    for val in collection.find({"Title": "Pink World"}):
       result.append(str(val))

    return result

@views.route('/create-hardcoded', methods=['GET', 'POST'])
def create_hardcoded():
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        abc = True

    response = '{response : 200}'
    collection = db.Songcollection
    collection.insert_one({
        "SongNumber": 10,
        "SongID": "SOUDSGM12AC9618304",
        "AlbumID": 692313,
        "AlbumName": "Superinstrumental",
        "ArtistID": "ARNTLGG11E2835DDB9",
        "ArtistLatitude": "",
        "ArtistLocation": "",
        "ArtistLongitude": "",
        "ArtistName": "Clp",
        "Danceability": 0.0,
        "Duration": 266.39628,
        "KeySignature": 7,
        "KeySignatureConfidence": 0.053,
        "Tempo": 114.041,
        "TimeSignature": 4,
        "TimeSignatureConfidence": 0.878,
        "Title": "Insatiable (Instrumental Version)",
        "Year": 0
    })
    result = []
    for val in collection.find():
       result.append(str(val))

    return result

@views.route('/update-hardcoded', methods=['GET', 'POST'])
def update_hardcoded():
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        abc = True

    response = '{response : 200}'

    collection = db.Songcollection
    collection.update_one({"SongID":"SOHKNRJ12A6701D1F8"}, {"$set" : {'Year': 1995}})
    result = []
    for val in collection.find():
        result.append(str(val))

    return result

@views.route('/delete-hardcoded', methods=['GET', 'POST'])
def delete_hardcoded():
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        abc = True

    response = '{response : 200}'

    collection = db.Songcollection
    collection.delete_one({"SongID": "SONHOTT12A8C13493C"})
    result = []
    for val in collection.find():
        result.append(str(val))

    return result