from flask import Flask, jsonify, request, render_template, url_for
from destinations import destinations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/destinations')
def getDestinations():
    return jsonify({ 'destinations': destinations })

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
        new_destination = {
            'city': request.json['city'],
            'country': request.json['country'],
            'description': request.json['description']
        }

        destinations.append(new_destination)

        return jsonify({'message': 'ok'})

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

