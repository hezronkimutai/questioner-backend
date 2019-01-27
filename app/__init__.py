import os
from  flask import Flask
from flask_restful import Api
from flask_restful import Resource
'''from app.api.v1.views.questionRecordViews import v1_questions_blueprint
from app.api.v1.views.meetupRecordViews import v1_meetup_blueprint
from app.api.v1.views.userRecordViews import v1_user_blueprint'''


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
from app.views.questionRecordViews import *
'''app.register_blueprint(v1_questions_blueprint)
app.register_blueprint(v1_meetup_blueprint)
app.register_blueprint(v1_user_blueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True'''
