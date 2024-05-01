from config.dbconfig import pg_config
import psycopg2

class piDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (
            pg_config['dbname'],
            pg_config['user'],
            pg_config['password'],
            pg_config['dbport'],
            pg_config['host'])
        self.conn = psycopg2.connect(connection_url)

    def getAllPI(self):
        cursor = self.conn.cursor()
        result = []
        query = 'select pi_id, user_id, pi_ipmain, pi_location, pi_ip, pi_status from "pestpis"'
        cursor.execute(query)
        for row in cursor:
            #print("row: ", row)
            result.append(row)
        return result
    
    #This is the Top 3 locations stat

    def getTop3Locations(self):
        cursor = self.conn.cursor()
        result = []
        query = 'SELECT pi_location, COUNT(*) AS location_count\
                FROM pestpis\
                GROUP BY pi_location\
                ORDER BY location_count DESC\
                LIMIT 3;'
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        return result
		
    
    def insertPI(self, user_id, pi_ipmain, pi_location, pi_ip, pi_status):
        cursor = self.conn.cursor()
        #validation check for dependencies/references exist
        query = 'insert into "pestpis"(user_id, pi_ipmain, pi_location, pi_ip, pi_status) values (%s,%s,%s,%s,%s) returning pi_id;'
        # 'insert into "pestpis"(user_id,pi_ipmain,ip_location,pi_ip,pi_status) values (%s,%s,%s,%s,%s) returning pi_id;'
        cursor.execute(query,(user_id, pi_ipmain, pi_location, pi_ip, pi_status,))
        pi_id = cursor.fetchone()[0]
        self.conn.commit()
        return pi_id

    def searchByID(self, pi_id):
        cursor = self.conn.cursor()
        query = 'select pi_id, user_id, pi_ipmain, pi_location, pi_ip, pi_status from "pestpis" where pi_id = %s'
        cursor.execute(query,(pi_id,))
        result = cursor.fetchone()
        return result
		
        
    def updateById(self, pi_id, user_id, pi_ipmain, pi_location, pi_ip, pi_status):
        cursor = self.conn.cursor()
        query = 'update "pestpis" set user_id = %s, pi_ipmain = %s, pi_location = %s, pi_ip = %s, pi_status = %s where pi_id = %s;'
        cursor.execute(query,(user_id, pi_ipmain, pi_location, pi_ip, pi_status, pi_id,))
        count = cursor.rowcount
        self.conn.commit()
        return count

    def deleteById(self,pi_id):
        cursor = self.conn.cursor()
        query = 'delete from "pestpis" where pi_id = %s'
        cursor.execute(query,(pi_id,))
        count = cursor.rowcount
        self.conn.commit()
        return count
    