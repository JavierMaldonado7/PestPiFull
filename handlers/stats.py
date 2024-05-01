from flask import jsonify
from dao.statsdao import statsDAO

# This class will mostly handle the jsonify formatting of all the functions
# that will be implemented by the DAO, it calls the DAO to get
# data from the tables and then formats them for the output.

class StatsHandler:

    """
    This section prepares the jsonify format using the attributes in alerts
    which is found on the schema
    """
    def build_lastalert_dict(self,row):
        result = {}
        result['alert_id'] = row[0]
        result['user_id'] = row[1]
        result['alert_date'] = row[2]
        result['alert_isActive'] = row[3]
        return result
    
    def build_gettop_dict(self, row) :
        result = {}
        result['alert_type'] = row[0]
        result['pi_location'] = row[1]
        result['alert_count'] = row[2]
        return result
    
    def build_getsightings_dict(self, row):
        result = {}
        result['alert_type'] = row[0]
        result['pi_location'] = row[1]
        result['sightings_count'] = row[2]
        result['last_sighting'] = row[3]
        return result
    

    
    # This section prepares the jsonify to get an Alert based on the provided parameter
    # Which could be: alert_id, user_id, alert_date, or alert_isActive

    def getLastAlert(self):
        dao = statsDAO
        alerts_list = dao.getLastAlert()
        result_list = []
        for row in alerts_list:
            result_list.append(self.build_lastalert_dict(row))
        return jsonify({"LastAlert" : result_list}), 200
    
    def getTop3(self, species):
        dao = statsDAO
        alerts_list = dao.getTop3(species)
        result_list = []
        for row in alerts_list:
            result_list.append(self.build_gettop_dict(row))
        return jsonify({"Top3" : result_list}), 200
    
    def getSightings(self, species, location, time ):
        dao = statsDAO
        alerts_list = dao.getTop3(species, location, time)
        result_list = []
        for row in alerts_list:
            result_list.append(self.build_getsightings_dict(row))
        return jsonify({"Top3" : result_list}), 200