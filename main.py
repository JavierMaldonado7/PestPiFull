from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from os import makedirs

from handlers.users import UserHandler
from handlers.pestpi import piHandler

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
    
# pestpis : get update delete
@app.route('/TEAMNAME/pestpi/<int:pi_id>', methods=["GET", "PUT", "DELETE"])
def searchByPIid(pi_id):
    if request.method == "GET":
        return piHandler().getPIbyId(pi_id)
    elif request.method == "PUT":
        args = request.json
        return piHandler().updatePI(pi_id,args)
    elif request.method == "DELETE":
        return piHandler().deletePI(pi_id)
    else:
        return jsonify("Not supported"), 405
#pestpis : insert/post 
@app.route('/TEAMNAME/pestpi', methods=["GET", "POST"])
def getallPI():
    if request.method == "GET":
        return piHandler().getAllPI()
    elif request.method == "POST":
        args = request.json
        return piHandler().insertPI(args)
    else:
        return jsonify("Not supported"), 405
    
# statistics=============================================================================
@app.route('/TEAMNAME/stats/alerts', methods=["GET"])
def getLastAlert():
    if request.method == "GET":
        #return statHandler().getLastAlert()
        return jsonify("Incomplete / Not supported"), 405
    else: 
        return jsonify("Not supported"), 405

@app.route('/TEAMNAME/top3location', methods=["POST"])
def top3locations():
    if request.method == 'POST':
        data = request.json
        #return statHandler().getTop3(data)
        return jsonify("Incomplete / Not supported"), 405
    else:
        return jsonify("Not supported"), 405

@app.route('/TEAMNAME/topsightings', methods=["POST"])
def topSightings():
    if request.method == 'POST':
        data = request.json
        #return statHandler().getTopSightings(data)
        return jsonify("Incomplete / Not supported"), 405
    else:
        return jsonify("Not supported"), 405
    
if __name__ == "__main__":
    app.debug = True
    app.run()