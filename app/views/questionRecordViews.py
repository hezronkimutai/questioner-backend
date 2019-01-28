
from flask import jsonify, Blueprint, request, json, abort, make_response
from ..models.questionRecordModels import Questions , all_questions
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
        title =question_args['title']
        body = question_args['body']
        question = Questions()
        question.create_question(title ,body)
        return  all_questions, 201


class Upvote(Resource):
    def patch(self , qstnId):
        question = Questions()
        upvte = question.upvote(qstnId)
        return {"status": 200, "data": upvte}, 200


class Downvote(Resource):
    def patch(self ,qstnId):
        question = Questions()
        dwnvte = question.downvote(qstnId)
        return {"status": 200, "data": dwnvte}, 200


class SingleQuestion(Resource):
    def get(self , qstnId):
        question = Questions()
        all_questions = question.get_all_questions()
        for single_question in all_questions:
            if single_question["qstnId"] == qstnId:
                return { "qstnId": qstnId,
                        "createdOn": single_question["createdOn"],
                        "createdBy": single_question["createdBy"], # generate userId
                        #"meetupId": meetupId, # generate meetupId
                        "title": single_question["title"],
                        "body":single_question["body"],
                        "up_votes":single_question["up_votes"],
                        "down_votes":single_question["down_votes"]
                        }
        #return {"single_question":"singe_question"}




api.add_resource(QuestionRecord, '/questions')
api.add_resource(SingleQuestion, '/questions/<int:qstnId>')
api.add_resource(Upvote, '/questions/<int:qstnId>/upvote')
api.add_resource(Downvote, '/questions/<int:qstnId>/downvote')
