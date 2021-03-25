from model import destinationModel, destination
from utils.convert import listToDictionary

class DestinationController():
    def __init__(self):
        self.__model = destinationModel.DestinationModel()

    def getDestinations(self, id = 0):
        return listToDictionary(self.__model.destinations(id = id))

    def createDestination(self, json):
        if self.__validateKeys(json) == "bad":
            return "bad request 404"

        _destination = destination.Destination(json['city'], json['country'], json['description'])
        result = self.__model.create(_destination)
        
        return result

    def updateDestination(self, id, json):
        #if self.__validateKeys(json) == "bad":
            #return "bad request 404"

        return self.__model.update(id, destination.Destination(json['city'], 
            json['country'], json['description']))
        
    def __validateKeys(self, json):
        for key in ['city', 'country', 'description']:
            if key not in json:
                return "bad"