import MySQLdb
class Base():
    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        self.conn = MySQLdb.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

def writeToBase(data:list) -> None:
    config = {
        'host' : 'localhost',
        'user' : 'HR',
        'password' : 'pass1234',
        'db' : 'base', 
        'charset' : 'utf8'
    }
    query = """INSERT INTO employees VALUES(%s, %s, %s, %s, %s);"""
    with Base(config) as base:
        base.execute(query, data)
    
def check(hashName:str, hashPass:str) -> bool:
    config = {
        'host' : 'localhost',
        'user' : 'Client',
        'password' : 'pass1234',
        'db' : 'base', 
        'charset' : 'utf8'
    }
    query = """SELECT * FROM employees; """
    with Base(config) as base:
        base.execute(query)
        datas = base.fetchall()
        for row in datas:
            if row[0] == hashName and row[1] == hashPass:
                return True


