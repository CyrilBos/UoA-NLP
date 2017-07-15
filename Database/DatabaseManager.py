import psycopg2, psycopg2.extras

class DatabaseManager:
    """
    Simple class using psycopg to allow retrieving data into dictionaries and not only lists.
    """
    def __init__(self, connect_string):
        """
        Initializes a new DatabaseManager instance with the given connection string.
        :param connect_string: provides database connection details : db name, user, password, ...
        :type connect_string: str
        """
        self.__connection = psycopg2.connect(connect_string)
        self.__cursor = self.__connection.cursor()
        self.__dict_cursor = self.__connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def select_query(self, query_string, query_data=None, fetch_to_dict=False):
        """
        Queries the prepared statement query_string with associated query_data through a Cursor if fetch_to_dict=False
        or through a DictCursor if True
        :param query_string: SQL prepared statement
        :type query_string: str
        :param query_data: data to fill query_string (may be None if query_string does not have parameters to be filled)
        :type query_data: tuple
        :param fetch_to_dict: if True the results will be returned as a dictionary, else as a list
        :type fetch_to_dict: bool
        :return: all the results from the executed query
        :rtype: Union[list,dict]
        """
        if not fetch_to_dict:
            curs = self.__cursor
        elif fetch_to_dict:
            curs = self.__dict_cursor
        else:
            curs = self.__cursor
        curs.execute(query_string, query_data)
        return curs.fetchall()

    def insert_query(self, query_str, query_data=None):
        self.__cursor.execute(query_str, query_data)
        self.__connection.commit()

    def close(self):
        """
        Manually closes the cursors and the connection to the database.
        """
        self.__connection.close()
        self.__cursor.close()
        self.__dict_cursor.close()