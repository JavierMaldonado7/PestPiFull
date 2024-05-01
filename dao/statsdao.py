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
    # SELECT alert_id, user_id, pi_id, species , alert_date
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
    # SELECT species, pi_location, COUNT(*) AS alert_count
    #  FROM alerts natural inner join pestpis
    #  WHERE species = %s
    #  GROUP BY pi_location
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
    # SELECT species, pi_location, COUNT(*) AS sightings_count, MAX(time) AS last_sighting
    # FROM alerts natural inner join pestpis
    # WHERE species = '%s'
    #   AND pi_location = '%s'
    #   AND time >= NOW() - INTERVAL '%s'
    # GROUP BY species, pi_location
    # ORDER BY sightings_count DESC
    # LIMIT 5;