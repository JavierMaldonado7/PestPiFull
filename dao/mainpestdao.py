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
    
    def getMainPestByIPMain(self, ip_main):
        cursor = self.conn.cursor()
        query = 'select main_id, user_id, main_ip, pi_ip from "mainpests" where ip_main = %s'
        cursor.execute(query, (ip_main,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    
    # This section handles the insert, delete and update queries

    def insertMainPest(self, alert_id, pi_id, ip_main):
        cursor = self.conn.cursor()
        query = 'insert into "mainpests"(alert_id, pi_id, ip_main) values (%s, %s, %s) returning model_id;'
        cursor.execute(query, (alert_id, pi_id, ip_main,))
        model_id = cursor.fetchone()[0]
        self.conn.commit()
        return model_id 
      
    def deleteMainPest(self, model_id):
        cursor = self.conn.cursor()
        query = 'delete from "mainpests" where model_id = %s;'
        cursor.execute(query, (model_id,))
        self.conn.commit()
        return model_id 
    
    def updateMainPest(self, model_id, alert_id, pi_id, ip_main):
        cursor = self.conn.cursor()
        query = 'update "mainpests" set alert_id = %s, pi_id = %s, ip_main = %s where model_id = %s;'
        cursor.execute(query, (alert_id, pi_id, ip_main,model_id,))
        self.conn.commit()
        return model_id 
    
    #Complex queries go here
    
    
    