from model import connection, destination

class DestinationModel():
    def __init__(self):
        self.__connection = connection.Connection()
        self.__connection.connect()
        self.__cursor =  self.__connection.getCursor()

    def destinations(self, id = 0):
        self.__cursor.execute(f'''select Id, City, Country, Description, Status, 
            DATE_FORMAT(CreationDate, "%d/%m/%Y %H:%i:%s") as CreationDate 
            from Destination where (IfNull({id}, 0) = 0 or {id} = Id) and Status = 1''')

        return self.__cursor.fetchall()

    def create(self, destination: destination.Destination):
        query = '''insert into Destination (City, Country, Description, Status) 
            values (%s, %s, %s, %s)'''

        try:
            self.__cursor.execute(query, (destination.city, destination.country, destination.description, 1))
            self.__connection.getConnection().commit()
        except Exception:
            return "problemas al insertar destino"
        else:
            #para obtener el id
            return self.__cursor.lastrowid

    def update(self, id, destination: destination.Destination):
        query = f'''update Destination set City = %s, 
                        Country = %s, Description = %s
                    where Id = {id}'''
        try:
            self.__cursor.execute(query, (destination.city, destination.country, destination.description, 1))
            self.__connection.getConnection().commit()
        except Exception as ex:
            return f"problemas actualizar - {ex}"
        else:
            return id



        