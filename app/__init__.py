import os
from  flask import Flask
from flask_restful import Api
from flask_restful import Resource

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
from app.views.questionRecordViews import *
from app.views.meetupRecordViews import *
from app.views.userRecordViews import *
