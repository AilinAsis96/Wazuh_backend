

import json


class UserModel():
    @classmethod
    def get_users(self):
        try:
            with open('users.json') as file:
                usr = json.load(file)
            return usr
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_user(self, user_id):
        try:
            with open('users.json') as file:
                usr = json.load(file)
            for i in usr:
                if (str(i['id']) == user_id):
                    return i
            return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_tasks(self, user_id):
        try:
            with open('tasks.json') as file:
                tasks = json.load(file)
            tasks_list = []    
            for i in tasks:
                if (str(i['user_id']) == user_id):
                    tasks_list.append(i)
            return tasks_list
        except Exception as ex:
            raise Exception(ex)