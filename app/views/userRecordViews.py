
from flask import jsonify, Blueprint, request, json, abort, make_response
from ..models.userRecordModels import UserRecord , all_users
from datetime import datetime
from uuid import uuid4
from flask_restful import Resource , reqparse
from app import api,app

user_parser = reqparse.RequestParser()
user_parser.add_argument('full_name', type=str, help='Enter your full name', required=True)
user_parser.add_argument('email', type=str, help='Enter your email', required=True)
user_parser.add_argument('username', type=str, help='Enter your username', required=True)
user_parser.add_argument('password', type=str, help='Enter your password', required=True)
user_parser.add_argument('repeat_password', type=str, help='Repeat your password' , required=True)

login_parser = reqparse.RequestParser()
login_parser.add_argument('login_email', type=str, help='Please enter the email', required=True)
login_parser.add_argument('login_password', type=str, help='please enter the password', required=True)


class SignupUser(Resource):
    def get(self):
        return {"All_users":"All_users"}

    def post(self):
        user_args = user_parser.parse_args()
        '''todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id'''
        full_name =user_args['full_name']
        email = user_args['email']
        username = user_args['username']
        password = user_args['password']
        repeat_password = user_args['repeat_password']
        user = UserRecord()
        user.create_user(full_name , email , username , password , repeat_password)
        return all_users, 201

class UserLogin(Resource):
    def get(self):
        registered_users = UserRecord()
        return registered_users.get_all_users()

    def post(self):
        login_args = login_parser.parse_args()
        login_email = login_args['login_email']
        login_password = login_args['login_password']
        registered_users = UserRecord()
        allusers = registered_users.get_all_users()
        for user in allusers:
            if "email" in user.keys():
                if user["email"]==login_email:
                    if  "password" in user.keys():
                        if user["password"]==login_password :
                            return {"message":"logged in successfully"},200
                        else:
                            return {"message":"incorrect credentials"}




class Singleuser(Resource):
    def get(self):
        return {"single_user":"singe_user"}



api.add_resource(UserLogin, '/login')
'''api.add_resource(UserLogout, '/logout')
api.add_resource(ResetPassword, '/reset-password')'''
api.add_resource(SignupUser, '/users')
api.add_resource(Singleuser, '/user')
