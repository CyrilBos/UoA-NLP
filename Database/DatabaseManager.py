import psycopg2, psycopg2.extras

class DatabaseManager:
    def __init__(self, connect_string):
        self.__connection = psycopg2.connect(connect_string)
        self.__cursor = self.__connection.cursor()
        self.__dict_cursor = self.__connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def my_query(self, query_string, query_data, fetch_to_dict=0):
        if not fetch_to_dict:
            curs = self.__cursor
        elif fetch_to_dict:
            curs = self.__dict_cursor
        else:
            curs = self.__cursor
        curs.execute(query_string, query_data)
        return curs.fetchall()

    def close(self):
        self.__connection.close()
        self.__cursor.close()
        self.__dict_cursor.close()