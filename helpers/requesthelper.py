from flask import request,jsonify

class requesthelper:
    def __init__(self) -> None:
        pass

    def requestBody():
        contentType = request.headers.get('Content-Type')
        if(contentType == 'application/json'):
            return request.json
        else:
            return jsonify({'message': 'Please include Content-Type as json'}), 400