from config.dbconfig import pg_config
import psycopg2

class MainPestDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (
            pg_config['dbname'],
            pg_config['user'],
            pg_config['password'],
            pg_config['dbport'],
            pg_config['host'])
        self.conn = psycopg2.connect(connection_url)

    # This section handles all the basic GET queries 

    def getAllMainPests(self):
        cursor = self.conn.cursor()
        query = 'select main_id, user_id, main_ip, pi_ip from mainpests'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        
    
    def getMainPestById(self, model_id):
        cursor = self.conn.cursor()
        query = 'select main_id, user_id, main_ip, pi_ip from "mainpests" where main_id = %s'
        cursor.execute(query, (model_id,))
        result = cursor.fetchone()
        return result

    def getMainPestByPestPiById(self, pi_id):
        cursor = self.conn.cursor()
        query = 'select main_id, user_id, main_ip, pi_ip from "mainpests" where pi_id = %s'
        cursor.execute(query, (pi_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getMainPestByAlertById(self, alert_id):
        cursor = self.conn.cursor()
        query = 'select main_id, user_id, main_ip, pi_ip from "mainpests" where alert_id = %s'
        cursor.execute(query, (alert_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getMainPestByMainIp(self, main_ip):
        cursor = self.conn.cursor()
        query = 'select main_id, user_id, main_ip, pi_ip from "mainpests" where main_ip = %s'
        cursor.execute(query, (main_ip,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    
    # This section handles the insert, delete and update queries

    def insertMainPest(self, user_id, main_ip, pi_ip):
        cursor = self.conn.cursor()
        query = 'insert into "mainpests"(user_id, main_ip, pi_ip)  values (%s, %s, %s) returning main_id;'
        cursor.execute(query, (user_id, main_ip, pi_ip,))
        main_id = cursor.fetchone()[0]
        self.conn.commit()
        return main_id
      
    def deleteMainPest(self, main_id):
        cursor = self.conn.cursor()
        query = 'delete from "mainpests" where main_id = %s;'
        cursor.execute(query, (main_id,))
        self.conn.commit()
        return main_id
    
    def updateMainPest(self, main_id, user_id, main_ip, pi_ip):
        cursor = self.conn.cursor()
        query = 'update "mainpests" set user_id = %s, main_ip = %s, pi_ip = %s where main_id = %s;'
        cursor.execute(query, (user_id, main_ip, pi_ip, main_id))
        self.conn.commit()
        return main_id
    
    #Complex queries go here
    
    
    