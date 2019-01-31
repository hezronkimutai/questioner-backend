
from flask import jsonify, Blueprint, request, json, abort, make_response
from ..models.commentRecordModels import Comment, all_comments
from datetime import datetime
from uuid import uuid4
from flask_restful import Resource , reqparse
from app import api,app

comment_parser = reqparse.RequestParser()
comment_parser.add_argument('comment', type=str, help='Please enter your comment', required=True)


class CommentRecord(Resource):
    def get(self):
        return {"all_comments":"all_comments"}

    def post(self):
        comment_args = comment_parser.parse_args()
        comment = comment_args['comment']
        comment = Comment()
        comment.create_comment(comment)
        return  comment, 200

api.add_resource(CommentRecord, '/questions/<int:qstnId>')
