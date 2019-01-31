from flask import jsonify, abort
from datetime import datetime
from uuid import uuid4
all_comments = []
class Comment:
    """  """
    def __init__(self, *args):
        self.all_comments_records = all_comments

    def create_comment(self,comment):
        """ Adds a new question to the all_question_records list """


        new_comment = {
            "created_on":str(datetime.now()),
            "comment":comment,
        }
        self.all_comments_records.append(new_comment)

    '''def fetch_single_meetup(self, meetupId):
        """ Fetches a single meetup based on the meetupId"""
        for meetup in self.all_meetup_records:
            if meetupId == int(meetupId):
                return meetup
            return abort(404, "Error: Meetup {} does'nt exist.".format(meetupId))'''
