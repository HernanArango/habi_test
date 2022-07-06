from engines.mysql import MySQL

engine = MySQL()


class DB:

    def query(self, sql, params):
        return engine.query(sql, params)

    def delete(self):
        pass

    def update(self):
        pass

    def insert(self):
        pass

