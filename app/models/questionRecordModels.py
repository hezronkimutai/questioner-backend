from flask import jsonify, Blueprint, request, json
from datetime import datetime
from uuid import uuid4
all_questions = []
up_votes_record = 0
down_votes_record=0

class Questions():
    """ Creates the question record model """
    def __init__(self, *args):
        self.all_question_records = all_questions
        self.up_votes = up_votes_record
        self.down_votes = down_votes_record
    def create_question(self, title, body,):
        """ Adds a new question to the all_question_records list """
        #votes = self.votes
        now = str(datetime.now())
        new_question = {
            "qstnId": len(self.all_question_records) + 1,
            "createdOn": now,
            "createdBy": uuid4().int, # generate userId
            #"meetupId": meetupId, # generate meetupId
            "title": title,
            "body":body,
            "up_votes": self.up_votes,
            "down_votes": self.down_votes
        }
        if new_question:
            self.all_question_records.append(new_question)
        return new_question

    def get_all_questions(self):
        return self.all_question_records

    def upvote(self, qstnId):
        for qstn in self.all_question_records:
            if qstn['qstnId'] == qstnId:
                qstn['up_votes'] = qstn['up_votes'] + 1
                return {"message" : "Voted up successfully"}

    def downvote(self, qstnId):
        for qstn in self.all_question_records:
            if qstn['qstnId'] == qstnId:
                qstn['down_votes'] = qstn['down_votes'] + 1
                return {"message" : "Voted down successfully"}
