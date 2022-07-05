
from flask import Blueprint, jsonify

#Models

from models.TaskModel import TaskModel


main=Blueprint('task_blueprint', __name__)

@main.route('/') 
def get_tasks():
    try:
        users = TaskModel.get_tasks()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<string:id>') 
def get_task(id):
    try:
        user = TaskModel.get_task(id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({}), 404    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500