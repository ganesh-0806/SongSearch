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

@views.route('/read/', methods=['GET', 'POST'])
def read():
    print('read called')
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        abc = True
    song_id = request.form['view-song-id']
    if not song_id:
        return
    response = '{response : 200}'
    collection = db.Songcollection
    result = []
    for val in collection.find({song_id}):
       result.append(str(val))

    return result

@views.route('/create/', methods=['GET', 'POST'])
def create():
    print('create called')
    if request.method == 'POST':
        #Interact with db and get details
        create_txt = request.form['create-text-area']
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
        abc = True
    response = '{response : 200}'


@views.route('/update/', methods=['GET', 'POST'])
def update():
    print('update called')
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        abc = True

    upd_id = request.form['update-song-id']
    upd_text = request.form['update-text-area']
    response = '{response : 200}'

    if not upd_id or not upd_text:
        return

    collection = db.Songcollection
    collection.update_one({"SongID": upd_id}, {"$set" : upd_text})
    result = []
    for val in collection.find():
        result.append(str(val))

    return result

@views.route('/delete/', methods=['GET', 'POST'])
def delete():
    print("delete called")
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        abc = True
    del_id = request.form['delete-song-id']
    response = '{response : 200}'
    del_str = ""
    if not del_id:
        return
    collection = db.Songcollection
    collection.delete_one({"SongID": del_id})
    result = []
    for val in collection.find():
        result.append(str(val))

    return result