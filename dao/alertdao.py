from config.dbconfig import pg_config
import psycopg2

class AlertDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (
            pg_config['dbname'],
            pg_config['user'],
            pg_config['password'],
            pg_config['dbport'],
            pg_config['host'])
        self.conn = psycopg2.connect(connection_url)

    # This section handles all the basic GET queries 

    def getAllAlerts(self):
        cursor = self.conn.cursor()
        query = 'select alert_id, user_id, pi_id, alert_type, alert_date, alert_isActive from "alerts"'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllActiveAlerts(self): #needs handler!
        cursor = self.conn.cursor()
        query = 'select alert_id, user_id, pi_id, alert_type, alert_date, alert_isActive from "alerts" where alert_isActive = true'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAlertById(self, alert_id):
        cursor = self.conn.cursor()
        query = 'select alert_id, user_id, pi_id, alert_type, alert_date, alert_isActive from "alerts" where alert_id = %s'
        cursor.execute(query, (alert_id,))
        result = cursor.fetchone()
        return result
       

    def getAlertByUserById(self, user_id):
        cursor = self.conn.cursor()
        query = 'select alert_id, user_id, pi_id, alert_type, alert_date, alert_isActive from "alerts" where user_id = %s'
        cursor.execute(query, (user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAlertByPiId(self, pi_id):
        cursor = self.conn.cursor()
        query = 'select alert_id, user_id, pi_id, alert_type, alert_date, alert_isActive from "alerts" where pi_id = %s'
        cursor.execute(query, (pi_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAlertByAlertType(self, alert_type):
        cursor = self.conn.cursor()
        query = 'select alert_id, user_id, pi_id, alert_type, alert_date, alert_isActive from "alerts" where alert_type = %s'
        cursor.execute(query, (alert_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    

    
    def getAlertByDate(self, alert_date):
        cursor = self.conn.cursor()
        query = 'select alert_id, user_id, pi_id, alert_type, alert_date, alert_isActive from "alerts" where alert_date = %s'
        cursor.execute(query, (alert_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAlertByIsActive(self, alert_isActive):
        cursor = self.conn.cursor()
        query = 'select alert_id, user_id, pi_id, alert_type, alert_date, alert_isActive from "alerts" where alert_isActive = %s'
        cursor.execute(query, (alert_isActive,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    # This section handles the insert, delete and update queries

    def insertAlert(self, user_id, pi_id, alert_type, alert_date, alert_isActive):
        cursor = self.conn.cursor()
        query = 'insert into "alerts"(user_id, pi_id, alert_type, alert_date, alert_isActive) values (%s, %s, %s, %s, %s) returning alert_id'
        cursor.execute(query, (user_id, pi_id, alert_type, alert_date, alert_isActive,))
        alert_id = cursor.fetchone()[0]
        self.conn.commit()
        return alert_id 
    
    def deleteAlert(self, alert_id):
        cursor = self.conn.cursor()
        query = 'delete from "alerts" where alert_id = %s;'
        cursor.execute(query, (alert_id,))
        self.conn.commit()
        return alert_id 
    
    def updateAlert(self, alert_id, user_id, pi_id, alert_type, alert_date, alert_isActive):
        cursor = self.conn.cursor()
        query = 'update "alerts" set user_id = %s, pi_id = %s, alert_type = %s, alert_date = %s, alert_isActive = %s where alert_id = %s;'
        cursor.execute(query, (user_id, pi_id, alert_type, alert_date, alert_isActive, alert_id,))
        self.conn.commit()
        return alert_id 
    
    # query = 'update "pestpis" set user_id = %s,pi_ipmain = %s,ip_location = %s,pi_ip = %s,pi_status = %s where pi_id = %s;'
        
    #Complex queries go here
    
    
    