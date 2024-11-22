import mysql.connector

class QueryError(Exception):
    pass

class MysqlConnector:
    def __init__(self):
        while True:
            try:
                self.__connection = mysql.connector.connect(

                                                                host="localhost",
                                                                user="leitor_termo",
                                                                password="termometria",
                                                                db="Termometria"
                                                            )
                if self.__connection.is_connected():
                    print("Connected.")
                    break
            except mysql.connector.Error as e:
                #print(f"Connection error: {e}")
                pass

    
    def __connect(self):
        return self.__connection
    

    def desconect(self):
        if self.__connection.is_connected():
            self.__connection.close()


    def get_query(self, query):
        if not self.__connection.is_connected or self.__connection.is_connected is None:
            self.__connection = self.__connect()
        cursor = self.__connection.cursor(dictionary=True)
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            raise QueryError(f"Error in query: {e}")
        finally:
           cursor.close()

           
    def set_query(self, query):
        if not self.__connection.is_connected or self.__connection.is_connected is None:
            self.__connection = self.__connect()
        cursor = self.__connection.cursor(dictionary=True)
        try:
            cursor.execute(query)
            self.__connection.commit()
        except mysql.connector.Error as e:
            raise QueryError(f"Error in query: {e}")
        finally:
            cursor.close()
