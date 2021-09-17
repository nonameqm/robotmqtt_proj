import psycopg2

class psqlController():
    def __init__(self, host="localhost", dbname="roboapi_db", user='salahdin', password='1234', port='5432'):
        try:
            self.host=host
            self.dbname=dbname
            self.user=user
            self.password=password
            self.port=port
            self.db=psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
            self.cursor=self.db.cursor()
        except:
            print("Not connected! Building Psql Controller Failed")

    def command_insert(self, command_line :str):
        try:
            self.cursor.execute(command_line)
        except psycopg2.OperationalError as oe:
            print(oe)

    def command_selectAll(self, table: str):
        try:
            self.cursor.execute("SELECT * FROM %s"%table)
            rows=self.cursor.fetchall()
            print(rows)
        except psycopg2.OperationalError as oe:
            print(oe)

