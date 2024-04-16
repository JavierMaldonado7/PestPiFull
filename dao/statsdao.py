from config.dbconfig import pg_config
import psycopg2

class statsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (
            pg_config['dbname'],
            pg_config['user'],
            pg_config['password'],
            pg_config['dbport'],
            pg_config['host'])
        self.conn = psycopg2.connect(connection_url)

    def getLastAlert(self):
        cursor = self.conn.cursor()
        result = []
        query = 'nothin yet'
        cursor.execute(query)
        for row in cursor:
            #print("row: ", row)
            result.append(row)
        return result
    # SELECT *
    # FROM alerts
    # ORDER BY time DESC
    # LIMIT 5;

    def getTop3(self,species):
        cursor = self.conn.cursor()
        result = []
        query = 'nothin yet'
        cursor.execute(query,(species,))
        for row in cursor:
            #print("row: ", row)
            result.append(row)
        return result
    # SELECT species, location, COUNT(*) AS alert_count
    #  FROM alerts
    #  WHERE species = %s
    #  GROUP BY location
    #  ORDER BY alert_count DESC
    #  LIMIT 3);

    def getSightings(self, species, location, time):
        cursor = self.conn.cursor()
        result = []
        query = 'nothin yet'
        cursor.execute(query,(species,location, time,))
        for row in cursor:
            #print("row: ", row)
            result.append(row)
        return result
    # SELECT species, location, COUNT(*) AS sightings_count, MAX(time) AS last_sighting
    # FROM alerts
    # WHERE species = '%s'
    #   AND location = '%s'
    #   AND time >= NOW() - INTERVAL '%s'
    # GROUP BY species, location
    # ORDER BY sightings_count DESC
    # LIMIT 5;