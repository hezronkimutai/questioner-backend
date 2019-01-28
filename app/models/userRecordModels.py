
all_users = []

class UserRecord:
    def __init__(self):
        self.db = all_users

    def create_user(self,full_name,  email,username, password, repeat_password):
        new_user = {
            "full_name" : full_name,
            "email": email,
            "username": username,
            "password": password,
            "repeat_password": repeat_password
        }
        if new_user:
            self.db.append(new_user)
        return new_user

    def get_all_users(self):
        return self.db

    def get_single_user(self, username):
        usr = [usr for usr in all_users if usr[username] == username]
        if usr:
            return usr
        return None
