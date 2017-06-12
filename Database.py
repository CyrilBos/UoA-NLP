import psycopg2, psycopg2.extras

class DatabaseManager:
    def __init__(self, connect_string):
        self.__connection = psycopg2.connect(connect_string)
        self.__cursor = self.__connection.cursor()
        self.__dict_cursor = self.__connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def query(self, query_string, query_data, fetch_method='array'):
        if fetch_method == 'array':
            curs = self.__cursor
        elif fetch_method == 'dict':
            curs = self.__dict_cursor
        else:
            curs = self.__cursor
        curs.execute(query_string, query_data)
        return curs.fetchall()

    def close(self):
        self.__connection.close()
        self.__cursor.close()
        self.__dict_cursor.close()