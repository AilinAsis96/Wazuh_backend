
import json


class TaskModel():
    @classmethod
    def get_tasks(self):
        try:
            with open('tasks.json') as file:
                task = json.load(file)
            return task
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_task(self, id):
        try:
            with open('tasks.json') as file:
                task = json.load(file)

            for i in task:
                if (str(i['id']) == id):
                    return i
            return None
        except Exception as ex:
            raise Exception(ex)