from asyncio import Task
from cProfile import run
import os
from flask import Flask
from flask_cors import CORS
from config import config
from flask_swagger_ui import get_swaggerui_blueprint


#Routes
from routes import User
from routes import Task

app = Flask(__name__)
def page_not_found(error):
    return "<h1>Not found page</h1>"

# Settings

CORS(app)

#Swagger configs 
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Test Wazuh API"}
)

_port = os.environ.get('PORT', 5000)

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprint
    app.register_blueprint(User.main, url_prefix='/api/users')
    app.register_blueprint(Task.main, url_prefix='/api/tasks')
    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)

    #Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()


