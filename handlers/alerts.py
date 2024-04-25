from flask import jsonify
from dao.alertdao import AlertDAO

# This class will mostly handle the jsonify formatting of all the functions
# that will be implemented by the DAO, it calls the DAO to get
# data from the tables and then formats them for the output.

class AlertHandler:

    """
    This section prepares the jsonify format using the attributes in alerts
    which is found on the schema
    """
    def build_alert_dict(self,row):
        result = {}
        result['alert_id'] = row[0]
        result['user_id'] = row[1]
        result['pi_id'] = row[2]
        result['alert_type'] = row[3]
        result['alert_date'] = row[4]
        result['alert_isActive'] = row[5]
        return result
    
    def build_topsightingalert_dict(self, row):
        result = {}
        result['alert_type'] = row[0]
        result['alert_count'] = row[1]
        return result
    
    def build_alert_attributes(self, alert_id, user_id, pi_id, alert_type, alert_date, alert_isActive):
        result = {}
        result['alert_id'] = alert_id
        result['user_id'] = user_id
        result['pi_id'] = pi_id
        result['alert_type'] = alert_type
        result['alert_date'] = alert_date
        result['alert_isActive'] = alert_isActive
        return result
    
    # This section prepares the jsonify to get an Alert based on the provided parameter
    # Which could be: alert_id, user_id, alert_date, or alert_isActive

    def getAllAlerts(self):
        dao = AlertDAO()
        alerts_list = dao.getAllAlerts()
        result_list = []
        for row in alerts_list:
            result = self.build_alert_dict(row)
            result_list.append(result)
        return jsonify({"Alerts" : result_list}), 200
    
    def getAlertById(self, alert_id):
        dao = AlertDAO()
        row = dao.getAlertById(alert_id)
        if not row:
            return jsonify(Error = "Alert Not Found"), 404
        else:
            alert = self.build_alert_dict(row)
            return jsonify({"Alert" : alert}), 200
        
    def getAlertByUserId(self, user_id):
        dao = AlertDAO()
        row = dao.getAlertByUserId(user_id)
        if not row:
            return jsonify(Error = "Alert Not Found"), 404
        else:
            alert = self.build_alert_dict(row)
            return jsonify({"Alert" : alert}), 200

    def getAlertByPiId(self, pi_id):
        dao = AlertDAO()
        row = dao.getAlertByPiId(pi_id)
        if not row:
            return jsonify(Error = "Alert Not Found"), 404
        else:
            alert = self.build_alert_dict(row)
            return jsonify({"Alert" : alert}), 200  

    def getAlertByAlertType(self, alert_type):
        dao = AlertDAO()
        row = dao.getAlertByAlertType(alert_type)
        if not row:
            return jsonify(Error = "Alert Not Found"), 404
        else:
            alert = self.build_alert_dict(row)
            return jsonify({"Alert" : alert}), 200     

        
    def getAlertByDate(self, alert_date):
        dao = AlertDAO()
        row = dao.getAlertByDate(alert_date)
        if not row:
            return jsonify(Error = "Alert Not Found"), 404
        else:
            alert = self.build_alert_dict(row)
            return jsonify({"Alert" : alert}), 200
    
    def getAlertByIsActive(self, alert_isActive):
        dao = AlertDAO()
        row = dao.getAlertByIsActive(alert_isActive)
        if not row:
            return jsonify(Error = "Alert Not Found"), 404
        else:
            alert = self.build_alert_dict(row)
            return jsonify({"Alert" : alert}), 200
        
    # This is the getLastAlert statistic 
    def getLastAlert(self):
        dao = AlertDAO()
        row = dao.getLastAlert()
        if not row:
            return jsonify(Error = "Alert Not Found"), 404
        else:
            alert = self.build_alert_dict(row)
            return jsonify({"Last Alert" : alert}), 200
        
    def getTopSightings(self):
        dao = AlertDAO()
        alerts_list = dao.getTopSightings()
        result_list = []
        for row in alerts_list:
            result = self.build_topsightingalert_dict(row)
            result_list.append(result)
        return jsonify({"Top Sightings" : result_list}), 200


        
    # This section handles the jsonify for inserting, deleting and updating a alert
        
    def insertAlert(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed Post Request"), 400
        else:
            user_id = form['user_id']
            pi_id = form['pi_id']
            alert_type = form['alert_type']
            alert_date = form['alert_date']
            alert_isActive = form['alert_isActive']

            if user_id and pi_id and alert_type and alert_date and alert_isActive:
                dao = AlertDAO()
                alert_id = dao.insertAlert(user_id, pi_id, alert_type, alert_date, alert_isActive)
                result = self.build_alert_attributes(alert_id ,user_id, pi_id, alert_type, alert_date, alert_isActive)
                return jsonify(Alert=result)
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400
            
    def deleteAlert(self, alert_id):
        dao = AlertDAO()
        if not dao.getAlertById(alert_id):
            return jsonify(Error = "Alert not found"), 404
        else:
            dao.deleteAlert(alert_id)
            return jsonify(DeleteStatus = "OK"), 200
    
    def updateAlert(self, alert_id, form):
        dao = AlertDAO()
        if not dao.getAlertById(alert_id):
            return jsonify(Error = "Malformed Update Request"), 400
        else:
           user_id = form['user_id']
           pi_id = form['pi_id']
           alert_type = form['alert_type']
           alert_date = form['alert_date']
           alert_isActive = form['alert_isActive']

           if user_id and pi_id and alert_type and alert_date and alert_isActive:
                dao = AlertDAO()
                alert_id = dao.updateAlert(user_id, pi_id, alert_type, alert_date, alert_isActive)
                result = self.build_alert_attributes(alert_id ,user_id, pi_id, alert_type, alert_date, alert_isActive)
                return jsonify(Alert=result)
           else:
                return jsonify(Error = "Unexpected attributes in post request"), 400
        
    
        
    
    
    
    