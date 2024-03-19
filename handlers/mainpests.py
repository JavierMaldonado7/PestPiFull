from flask import jsonify
from dao.mainpestdao import MainPestDAO

# This class will mostly handle the jsonify formatting of all the functions
# that will be implemented by the DAO, it calls the DAO to get
# data from the tables and then formats them for the output.

class MainPestHandler:

    """
    This section prepares the jsonify format using the attributes in alerts
    which is found on the schema
    """
    def build_mainpest_dict(self,row):
        result = {}
        result['model_id'] = row[0]
        result['alert_id'] = row[1]
        result['pi_id'] = row[2]
        result['ip_main'] = row[3]
        return result
    
    def build_mainpest_attributes(self, model_id, alert_id, pi_id, ip_main):
        result = {}
        result['model_id'] = model_id
        result['alert_id'] = alert_id
        result['pi_id'] = pi_id
        result['ip_main'] = ip_main
        return result
    
    # This section prepares the jsonify to get a MainPest based on the provided parameter
    # Which could be: model_id, alert_id,  pi_id, or ip_main

    def getAllMainPests(self):
        dao = MainPestDAO()
        mainpests_list = dao.getAllMainPests()
        result_list = []
        for row in mainpests_list:
            result = self.build_mainpest_dict(row)
            result_list.append(result)
        return jsonify({"MainPests" : result_list}), 200
    
    def getMainPestById(self, model_id):
        dao = MainPestDAO()
        row = dao.getMainPestById(model_id)
        if not row:
            return jsonify(Error = "MainPest Not Found"), 404
        else:
            mainpest = self.build_mainpest_dict(row)
            return jsonify({"MainPest" : mainpest}), 200
        
    def getMainPestByAlertById(self, alert_id):
        dao = MainPestDAO()
        row = dao.getMainPestByAlertById(alert_id)
        if not row:
            return jsonify(Error = "MainPest Not Found"), 404
        else:
            mainpest = self.build_mainpest_dict(row)
            return jsonify({"MainPest" : mainpest}), 200
        
    def getMainPestByPestPiById(self, pi_id):
        dao = MainPestDAO()
        row = dao.getMainPestByPestPiById(pi_id)
        if not row:
            return jsonify(Error = "MainPest Not Found"), 404
        else:
            mainpest = self.build_mainpest_dict(row)
            return jsonify({"MainPest" : mainpest}), 200
    
    def getMainPestByIPMain(self, ip_main):
        dao = MainPestDAO()
        row = dao.getMainPestByIPMain(ip_main)
        if not row:
            return jsonify(Error = "MainPest Not Found"), 404
        else:
            mainpest = self.build_mainpest_dict(row)
            return jsonify({"MainPest" : mainpest}), 200
        
    # This section handles the jsonify for inserting, deleting and updating a MainPest
        
    def insertMainPest(self, form):
        print("form: ", form)
        if len(form) != 3:
            return jsonify(Error = "Malformed Post Request"), 400
        else:
            alert_id = form['alert_id']
            pi_id = form['pi_id']
            ip_main = form['ip_main']

            if alert_id and pi_id and ip_main:
                dao = MainPestDAO()
                model_id = dao.insertMainPest(alert_id, pi_id, ip_main)
                result = self.build_mainpest_attributes(model_id ,alert_id, pi_id, ip_main)
                return jsonify(MainPest=result)
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400
            
    def deleteMainPest(self, model_id):
        dao = MainPestDAO()
        if not dao.getMainPestById(model_id):
            return jsonify(Error = "MainPest not found"), 404
        else:
            dao.deleteMainPest(model_id)
            return jsonify(DeleteStatus = "OK"), 200
    
    def updateMainPest(self, model_id, form):
        dao = MainPestDAO()
        if not dao.getMainPestById(model_id):
            return jsonify(Error = "Malformed Update Request"), 400
        else:
           alert_id = form['alert_id']
           pi_id = form['pi_id']
           ip_main = form['ip_main']
           
           if alert_id and pi_id and ip_main:
                dao = MainPestDAO()
                model_id = dao.updateMainPest(alert_id, pi_id, ip_main)
                result = self.build_mainpest_attributes(model_id ,alert_id, pi_id, ip_main)
                return jsonify(MainPest=result)
           else:
                return jsonify(Error = "Unexpected attributes in post request"), 400
        
    
        
    
    
    
    