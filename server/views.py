from flask import Blueprint, render_template, request, flash, jsonify
import json

views = Blueprint('views', __name__)


# Pseudo template
@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        #Interact with db and get details
        # jsonify the response
        abc = True

    response = '{response : 200}'
    
    return '<h1>This is home page </h1>'