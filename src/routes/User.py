
from flask import Blueprint, jsonify

#Models

from models.UserModel import UserModel


main=Blueprint('user_blueprint', __name__)

@main.route('/') 
def get_users():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<string:user_id>') 
def get_user(user_id):
    try:
        user = UserModel.get_user(user_id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({}), 404    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<string:user_id>/tasks') 
def get_tasks(user_id):
    try:
        tasks = UserModel.get_tasks(user_id)
        if tasks != []:
            return jsonify(tasks)
        else:
            return jsonify({}), 404    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
