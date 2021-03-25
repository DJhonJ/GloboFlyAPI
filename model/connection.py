import mysql.connector

class Connection():
    def __init__(self):
        self.__connection = None

    def connect(self):
        self.__connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="globofly"
        )
            

    def getCursor(self):
        if self.__connection == None:
            raise Exception("connection is null")

        return self.__connection.cursor()
    
    def getConnection(self):
        return self.__connection