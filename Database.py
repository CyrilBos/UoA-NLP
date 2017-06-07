import psycopg2

class DatabaseManager:
    def __init__(self, connect_string):
        self.__connection = psycopg2.connect(connect_string)
        self.__cursor = self.__connection.cursor()

    def query(self, query_string, query_data):
        self.__cursor.execute(query_string, query_data)
        return self.__cursor.fetchall()
