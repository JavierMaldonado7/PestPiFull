from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from os import makedirs

from handlers.users import UserHandler
from handlers.pestpi import piHandler
from handlers.mainpests import MainPestHandler
from handlers.alerts import AlertHandler
from handlers.stats import StatsHandler

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


#####################################
#This section is for the user routes
#####################################

# Insert(post) a user or get all users
@app.route('/capstone-pestpi/user', methods=["GET", "POST"])
def getAllUsers():
    if request.method == 'GET':
        return UserHandler().getAllUsers()
    elif request.method == 'POST':
        args = request.json
        return UserHandler().insertUser(args)
    else:
        return jsonify("Not supported"), 405


# Get a specific user, update a user and delete a user   
@app.route('/capstone-pestpi/user/<int:user_id>', methods=["GET", "PUT", "DELETE"])
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
    
#######################################
#This section is for the pestpi routes
#######################################

# Insert(post) a pestpi or get all pestpis
@app.route('/capstone-pestpi/pestpi', methods=["GET", "POST"])
def getAllPestPis():
    if request.method == 'GET':
        return piHandler().getAllPI()
    elif request.method == 'POST':
        args = request.json
        return piHandler().insertPI(args)
    else:
        return jsonify("Not supported"), 405

  
# Get a specific pestpi, update a pestpi and delete a pestpi
@app.route('/capstone-pestpi/pestpi/<int:pi_id>', methods=["GET", "PUT", "DELETE"])
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
    
#######################    
# Dashboard Statistics
#######################

#This statistic gets the Last Alert that was created
@app.route('/capstone-pestpi/stats/lastalert', methods=["GET"])
def getLastAlert():
    if request.method == 'GET':
        return AlertHandler().getLastAlert()
    else: 
        return jsonify("Not supported"), 405

#This statistic gets the Top 3 Locations 
@app.route('/capstone-pestpi/top3location', methods=["GET"])
def top3locations():
    if request.method == 'GET':
        return piHandler().getTop3Locations()
    else: 
        return jsonify("Not supported"), 405    

#This statistic gets the Top Sightings 
@app.route('/capstone-pestpi/topsightings', methods=["GET"])
def topSightings():
    if request.method == 'GET':
        return AlertHandler().getTopSightings()
    else: 
        return jsonify("Not supported"), 405    
    
if __name__ == "__main__":
    app.debug = True
    app.run()