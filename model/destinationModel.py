from model import connection, destination

class DestinationModel():
    def __init__(self):
        self.__connection = connection.Connection()
        self.__connection.connect()
        self.__cursor =  self.__connection.getCursor()

    def destinations(self):
        self.__cursor.execute('select * from Destination')
        ##self.__connection.getConnection().commit()
        
        return self.__cursor.fetchall()

    def create(self, destination: destination.Destination):
        query = 'insert into Destination (City, Country, Description, State) values (?,?,?,?)'
        self.__cursor.executemany(query, (destination.city, 
            destination.country, destination.description, 1))

        self.__connection.getConnection().commit()

        return "ok"
        