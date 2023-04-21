from flask import Blueprint, render_template, request, flash, jsonify
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