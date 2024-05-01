from config.dbconfig import pg_config
import psycopg2

class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (
            pg_config['dbname'],
            pg_config['user'],
            pg_config['password'],
            pg_config['dbport'],
            pg_config['host'])
        self.conn = psycopg2.connect(connection_url)

    # This section handles all the basic GET queries 

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = 'select user_id,user_name, user_email, user_password from "users"'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getUserById(self, user_id):
        cursor = self.conn.cursor()
        query = 'select user_id,user_name, user_email, user_password from "users" where user_id = %s'
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    def getUserByName(self, user_name):
        cursor = self.conn.cursor()
        query = 'select user_id,user_name, user_email, user_password from "users" where user_name = %s'
        cursor.execute(query, (user_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByEmail(self, user_email):
        cursor = self.conn.cursor()
        query = 'select user_id,user_name, user_email, user_password from "users" where user_email = %s'
        cursor.execute(query, (user_email,))
        result = []
        for row in cursor:
            result.append(row)
        return result 
    
    # This section handles the insert, delete and update queries

    def insertUser(self, user_name, user_email, user_password):
        cursor = self.conn.cursor()
        query = 'insert into "users"(user_name, user_email, user_password) values (%s, %s, %s) returning user_id;'
        cursor.execute(query, (user_name, user_email, user_password,))
        user_id = cursor.fetchone()[0]
        self.conn.commit()
        return user_id 
      
    
    def deleteUser(self, user_id):
        cursor = self.conn.cursor()
        query = 'delete from "users" where user_id = %s;'
        cursor.execute(query, (user_id,))
        self.conn.commit()
        return user_id 
    
    def updateUser(self, user_id, user_name, user_email, user_password):
        cursor = self.conn.cursor()
        query = 'update "users" set user_name = %s, user_email = %s, user_password = %s where user_id = %s;'
        cursor.execute(query, (user_name, user_email, user_password,user_id,))
        self.conn.commit()
        return user_id 
    
    #Complex queries go here

