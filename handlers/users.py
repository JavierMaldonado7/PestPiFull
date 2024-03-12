from flask import jsonify
from dao.userdao import UserDAO

# This class will mostly handle the jsonify formatting of all the functions
# that will be implemented by the DAO, it calls the DAO to get
# data from the tables and then formats them for the output.

class UserHandler:

    """
    This section prepares the jsonify format using the attributes in users
    which is found on the schema
    """
    def build_user_dict(self,row):
        result = {}
        result['user_id'] = row[0]
        result['user_name'] = row[1]
        result['user_email'] = row[2]
        result['user_password'] = row[3]
        return result
    
    def build_user_attributes(self, user_id, user_name, user_email, user_password):
        result = {}
        result['user_id'] = user_id
        result['user_name'] = user_name
        result['user_email'] = user_email
        result['user_password'] = user_password
        return result
    
    # This section prepares the jsonify to get a User based on the provided parameter
    # Which could be: user_id, user_name, user_email, or user_password
    
    def getAllUsers(self):
        dao = UserDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify({"Users" : result_list}), 200
    
    def getUserById(self, user_id):
        dao = UserDAO()
        row = dao.getUserById(user_id)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify({"User" : user}), 200

    def getUserByName(self, user_name):
        dao = UserDAO()
        row = dao.getUserByName(user_name)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify({"User" : user}), 200
    
    def getUserByEmail(self, user_email):
        dao = UserDAO()
        row = dao.getUserByEmail(user_email)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify({"User" : user}), 200
        
    def getUserByPassword(self, user_password):
        dao = UserDAO()
        row = dao.getUserByPassword(user_password)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify({"User" : user}), 200
        
    # This section handles the jsonify for inserting, deleting and updating a user
        
    def insertUser(self, form):
        print("form: ", form)
        if len(form) != 3:
            return jsonify(Error = "Malformed Post Request"), 400
        else:
            user_name = form['user_name']
            user_email = form['user_email']
            user_password = form['user_password']

            if user_name and user_email and user_password:
                dao = UserDAO()
                user_id = dao.insertUser(user_name, user_email, user_password)
                result = self.build_user_attributes(user_id, user_name, user_email, user_password)
                return jsonify(User=result)
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400
            
    def deleteUser(self, user_id):
        dao = UserDAO()
        if not dao.getUserById(user_id):
            return jsonify(Error = "User not found"), 404
        else:
            dao.deleteUser(user_id)
            return jsonify(DeleteStatus = "OK"), 200
        
    def updateUser(self, user_id, form):
        dao = UserDAO()
        if not dao.getUserById(user_id):
            return jsonify(Error = "Malformed Update Request"), 400
        else:
           user_name = form['user_name']
           user_email = form['user_email']
           user_password = form['user_password']

           if user_name and user_email and user_password:
                dao = UserDAO()
                user_id = dao.updateUser(user_name, user_email, user_password)
                result = self.build_user_attributes(user_id, user_name, user_email, user_password)
                return jsonify(User=result)
           else:
                return jsonify(Error = "Unexpected attributes in post request"), 400
            
    
        


    


