from model import destinationModel, destination

class DestinationController():
    def __init__(self):
        self.__model = destinationModel.DestinationModel()

    def getDestinations(self):
        return self.__model.destinations()

    def createDestination(self, json):
        for key in ['city', 'country', 'description']:
            if key not in json:
                return "bad request 404 - body"

        _destination = destination.Destination(json['city'], json['country'], json['description'])
        result = self.__model.create(_destination)
        
        return result

    


