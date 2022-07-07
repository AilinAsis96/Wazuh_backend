from asyncio import Task
from cProfile import run
from flask import Flask
from flask_cors import CORS
from config import config


#Routes
from routes import User
from routes import Task

app = Flask(__name__)
def page_not_found(error):
    return "<h1>Not found page</h1>"

# Settings
CORS(app)

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprint
    app.register_blueprint(User.main, url_prefix='/api/users')
    app.register_blueprint(Task.main, url_prefix='/api/tasks')

    #Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()


