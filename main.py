from flask import Flask, jsonify, request, render_template, url_for
from destinations import destinations
from controller.destinationController import DestinationController

app = Flask(__name__)

__destinationController = DestinationController()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/destinations')
def getDestinations():
    destinos = __destinationController.getDestinations()
    return jsonify({ 'destinations': destinos })

@app.route('/destinations/<int:id>')
def getDestination(id):
    for destination in destinations:
        if destination['id'] == id:
            return destination
        
    return jsonify({ 'message': 'Producto no encontrado' })

@app.route('/destination', methods=['POST'])
def addDestination():
    if request.json == None: 
        return jsonify({'message': 'Bad request'})
    else:   
        result = __destinationController.createDestination(request.json)

        return jsonify({'message': result})

@app.route('/destination/<int:id>', methods=['PUT'])
def updateDestination(id):
    def validate(listDestination, key, valueRequest):
        if key in valueRequest:
            listDestination[key] = valueRequest[key]

    for destination in destinations:
        if destination["id"] == id:
            validate(destination, "city", request.json)
            validate(destination, "country", request.json)
            validate(destination, "description", request.json)

            return jsonify({"message": "update ok"})
    
    return jsonify({"message": "destination not found."}) 

@app.route('/destination/<int:id>', methods=['DELETE'])
def deleteDestination(id):
    for destination in destinations:
        if id in destination.values():
            destination.clear()
            return jsonify({"message": "remove ok"})

    return jsonify({"message": "destination not found."}) 

if __name__ == '__main__':
    app.run(debug=True, port=5000)

