
from flask import jsonify, Blueprint, request, json, abort, make_response
from ..models.meetupRecordModels import Meetups , all_meetups
from datetime import datetime
from uuid import uuid4
from flask_restful import Resource , reqparse
from app import api,app

meetup_parser = reqparse.RequestParser()
meetup_parser.add_argument('meetup_title', type=str, help='Please enter meetup  title', required=True)
meetup_parser.add_argument('meetup_body', type=str, help='Enter your Question', required=True)


class MeetupRecord(Resource):
    def get(self):
        meetup = Meetups()
        meetups=meetup.get_all_meetups()
        return meetups, 201

    def post(self):
        meetup_args = meetup_parser.parse_args()
        title =meetup_args['meetup_title']
        body = meetup_args['meetup_body']
        if not title.strip():
            return {"message":"Please provide your title"},400
        if not body.strip():
            return {"message":"Please provide your meetup"},400
        meetup = Meetups()
        meetup=meetup.create_meetup(title ,body)
        return  all_meetups, 201

class SingleMeetup(Resource):
    def get(self, meetupId):
        single_meetup = Meetups()
        return single_meetup.fetch_single_meetup(self)



api.add_resource(MeetupRecord, '/meetups')
api.add_resource(SingleMeetup, '/meetups/<int:meetupId>')
