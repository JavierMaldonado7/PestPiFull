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
        query = "GOTTA REDO THE SQL QUERY;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getMainPestById(self, model_id):
        cursor = self.conn.cursor()
        query = "SELECT BLANK FROM BLANK where  = %s;"
        cursor.execute(query, (model_id,))
        result = cursor.fetchone()
        return result
    
    def getMainPestByIPMain(self, ip_main):
        cursor = self.conn.cursor()
        query = "GOTTA REDO THE SQL QUERY;"
        cursor.execute(query, (ip_main,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    
    # This section handles the insert, delete and update queries

    def insertMainPest(self, model_id, ip_main):
        cursor = self.conn.cursor()
        query = "insert into MainPest(model_id, ip_main) values (%s, %s, %s) returning model_id;"
        cursor.execute(query, (model_id, ip_main,))
        model_id = cursor.fetchone()[0]
        self.conn.commit()
        return model_id 
    
    def deleteMainPest(self, model_id):
        cursor = self.conn.cursor()
        query = "delete from MainPest where model_id = %s;"
        cursor.execute(query, (model_id,))
        self.conn.commit()
        return model_id 
    
    def updateMainPest(self, model_id, ip_main):
        cursor = self.conn.cursor()
        query = "update MainPest set model_id = %s, ip_main = %s;"
        cursor.execute(query, (model_id, ip_main,))
        self.conn.commit()
        return model_id 
    
    #Complex queries go here
    
    
    