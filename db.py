from engines.mysql import MySQL

engine = MySQL()


class DB:
    @staticmethod
    def query(sql, params=None):
        return engine.query(sql, params)

    def delete(self):
        pass

    def update(self):
        pass

    def insert(self):
        pass

