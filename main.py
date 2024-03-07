from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from os import makedirs

from handlers.users import UserHandler

app = Flask(__name__, instance_relative_config=True)

CORS(app, origins=["*"])  # allow it from all places

# ensure the instance folder exists
try:
    makedirs(app.instance_path)
except OSError:
    pass

#Test
# Home Page, greeting
@app.route('/')
def greeting():
    return 'Hello, this is the PestPi App!'

# Insert(post) a user or get all users
#TODO: get the heroku working with these directories
@app.route('/TEAMNAME/user', methods=["GET", "POST"])
def getAllUsers():
    if request.method == 'GET':
        return UserHandler().getAllUsers()
    elif request.method == 'POST':
        args = request.json
        return UserHandler().insertUser(args)
    else:
        return jsonify("Not supported"), 405


# Get a specific user, update a user and delete a user   
@app.route('/TEAMNAME/user/<int:user_id>', methods=["GET", "PUT", "DELETE"])
def searchByUserId(user_id):
    if request.method == "GET":
        return UserHandler().getUserByID(user_id)
    elif request.method == "PUT":
        args = request.json
        return UserHandler().updateUser(user_id, args)
    elif request.method == "DELETE":
        return UserHandler().deleteUser(user_id)
    else:
        return jsonify("Not supported"), 405