def listToDictionary(list: list):
    nuevaLista = []

    if len(list) > 0:
        for element in list:
            nuevaLista.append({
                'id': element[0],
                'city': element[1],
                'country': element[2],
                'description': element[3],
                'status': element[4],
                'creationdate': element[5]
            })

    return nuevaLista