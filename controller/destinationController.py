from model import destinationModel, destination

class DestinationController():
    def __init__(self):
        self.__model = destinationModel.DestinationModel()

    def getDestinations(self):
        return self.__model.destinations()

    def createDestination(self, city, country, description):
        _destination = destination.Destination(city, country, description)
        result = self.__model.create(_destination)
        
        return result

    


