import mysql.connector
import config


class MySQL:

    def connect(self):
        try:
            mydb = mysql.connector.connect(
                host=config.DB_HOSTNAME,
                port=config.DB_PORT,
                user=config.DB_USER,
                password=config.DB_PASSWORD
            )
            cursor = mydb.cursor()
            cursor.execute(f"use {config.DB_NAME}")
            return cursor, mydb
        except mysql.connector.Error as e:
            print(e)

    def query(self, sql, params):
        try:
            cursor, _ = self.connect()

            if params is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql, params)

            records = cursor.fetchall()
            return records
        except mysql.connector.Error as e:
            print(e)


