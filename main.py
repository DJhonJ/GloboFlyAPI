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
    destinos = __destinationController.getDestinations(0)
    return jsonify(destinos)

@app.route('/destinations/<int:id>')
def getDestination(id):
    return jsonify(__destinationController.getDestinations(id))

@app.route('/destination', methods=['POST'])
def addDestination():
    if request.json == None: 
        return jsonify({'message': 'Bad request'})
    else:   
        response = __destinationController.createDestination(request.json)

        return jsonify({'id': response, 'message': 'ok'})

@app.route('/destination/<int:id>', methods=['PUT'])
def updateDestination(id):
    if request.json == None: 
        return jsonify({'message': 'Bad request'})
    else:   
        for item in __destinationController.getDestinations(0):
            if item['id'] == id:
                response = __destinationController.updateDestination(id, request.json)
                return jsonify({ 'message': response })
        
        return jsonify({ 'message': 'destination not found.' })
        
@app.route('/destination/<id>', methods=['DELETE'])
def deleteDestination(id):
    print(id)
    for item in __destinationController.getDestinations(0):
        if item["id"] == int(id):
            respuesta = __destinationController.deleteDestination(id)
            return jsonify({ 'message': respuesta })
        
    return jsonify({ 'message': 'destination not found.' })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

