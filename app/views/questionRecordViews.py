
from flask import jsonify, Blueprint, request, json, abort, make_response
from ..models.questionRecordModels import QuestionRecord
from datetime import datetime
from uuid import uuid4
from flask_restful import Resource , reqparse
from app import api,app

question_parser = reqparse.RequestParser()
question_parser.add_argument('title', type=str, help='Please enter question title', required=True)
question_parser.add_argument('body', type=str, help='Enter your Question', required=True)


class QuestionRecord(Resource):
    def get(self):
        return {"All_questions":"All_questions"}

    def post(self):
        question_args = question_parser.parse_args()
        '''todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id'''
        TODOS = {'title': question_args['title'] , 'body': question_args['body']}
        return TODOS, 201



class SingleQuestion(Resource):
    def get(self):
        return {"single_question":"singe_question"}



api.add_resource(QuestionRecord, '/questions')
api.add_resource(SingleQuestion, '/question')