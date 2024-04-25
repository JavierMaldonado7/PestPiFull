from flask import jsonify
from dao.pidao import piDAO

class piHandler:
    def build_pi_dict(self,row):
        result = {}
        result['pi_id'] = row[0]
        result['user_id'] = row[1]
        result['pi_ipmain'] = row[2]
        result['pi_location'] = row[3]
        result['pi_ip'] = row[4]
        result['pi_status'] = row[5]
        return result
    
    def build_top3locationspi_dict(self, row):
        result = {}
        result['pi_location'] = row[0]
        result['location_count'] = row[1]
        return result

    def build_pi_attributes(self, pi_id, user_id, pi_ipmain, pi_location, pi_ip, pi_satus):
        result = {}
        result['pi_id'] = pi_id
        result['user_id'] = user_id
        result['pi_ipmain'] = pi_ipmain
        result['pi_location'] = pi_location
        result['pi_ip'] = pi_ip
        result['pi_status'] = pi_satus
        return result
    
    def getAllPI(self):
        dao = piDAO()
        pi_list = dao.getAllPI()
        result = []
        for row in pi_list:
            result.append(self.build_pi_dict(row))
        return jsonify(result)
    
    #This is the Top 3 Locations stat
    def getTop3Locations(self):
        dao = piDAO()
        pi_list = dao.getTop3Locations()
        result = []
        for row in pi_list:
            result.append(self.build_top3locationspi_dict(row))
        return jsonify(result)

    def insertPI(self,data):
        print("form: \n", data )
        user_id = data['user_id']
        pi_ipmain = data['pi_ipmain']
        ip_location = data['ip_location']
        pi_ip = data['pi_ip']
        pi_status = data['pi_status']
        if user_id and pi_ipmain and ip_location and pi_ip and pi_status:
            dao = piDAO()
            pi_id = dao.insertPI(user_id,pi_ipmain,ip_location,pi_ip,pi_status)
            data['pi_id'] = pi_id
            return jsonify(data),201
        else:
            return jsonify("Unexpected attribute values."), 400

    def getPIbyId(self,pi_id):
        dao = piDAO()
        result = dao.searchById(pi_id)
        if result:
            return jsonify(self.build_pi_dict(result))
        else:
            return jsonify("Not Found"),404

    def updatePI(self, pi_id,data):
        #print(data)
        user_id = data['user_id']
        pi_ipmain = data['pi_ipmain']
        ip_location = data['ip_location']
        pi_ip = data['pi_ip']
        pi_status = data['pi_status']
        if pi_id and user_id and pi_ipmain and ip_location and pi_ip and pi_status:
            dao = piDAO()
            flag = dao.updateById(pi_id,user_id,pi_ipmain,ip_location,pi_ip,pi_status)
            if flag:
                return jsonify(data),201
            else:
                return jsonify("Not Found"), 404
        else:
            return jsonify("Unexpected attribute values."), 400

    def deletePI(self,pi_id):
        dao = piDAO()
        result = dao.deleteById(pi_id)
        if result:
            return jsonify("OK"),200
        else:
            return jsonify("Not Found"),404
    
