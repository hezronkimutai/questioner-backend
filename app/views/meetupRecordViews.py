
from flask import jsonify, Blueprint, request, json, abort, make_response
from ..models.questionRecordModels import QuestionRecord
from datetime import datetime
from uuid import uuid4
from flask_restful import Resource , reqparse
from app import api,app

meetup_parser = reqparse.RequestParser()
meetup_parser.add_argument('meetup_title', type=str, help='Please enter question title', required=True)
meetup_parser.add_argument('meetup_body', type=str, help='Enter your Question', required=True)


class MeetupRecord(Resource):
    def get(self):
        return {"All_meetups":"All_meetups"}

    def post(self):
        meetup_args = question_parser.parse_args()
        '''todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id'''
        meetup = {'title': question_args['meetup_title'] , 'body': question_args['meetup_body']}
        return TODOS, 201



class SingleMeetup(Resource):
    def get(self):
        return {"single_meetup":"singe_meetup"}



api.add_resource(MeetupRecord, '/questions')
api.add_resource(SingleMeetup, '/question')
