import mysql.connector
import config


class MySQL:

    def __init__(self):
        self.cursor = self.connect()

    def connect(self):
        mydb = mysql.connector.connect(
            host=config.DB_HOSTNAME,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASSWORD
        )
        return mydb.cursor()

    def query(self, sql, params):
        return self.cursor.execute(sql)

