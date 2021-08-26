from exceptions.validationexception import ValidationException
from flask.json import jsonify
from auth import Auth
from flask import request
from helpers.requesthelper import requesthelper
from validator.loginvalidator import LoginValidator

def login():
    try:
        body = requesthelper.requestBody()
        list = LoginValidator.validate(body)
        auth = Auth(body['email'],body['password'])
        token = auth.login()
        return jsonify({'data': {
            'token' : token,
            'status': '200'
        }})
    except ValidationException as e:
        return jsonify({'errors': e.errors}), 422

    