from exceptions.validationexception import ValidationException
from helpers.jwthelper import JwtHelper
from flask import jsonify
import sys

class Auth:
    def __init__(self,email, password):
        self.email = email
        self.password = password
        self.key = "secret"

    def checkCreds(self):
        if self.email != 'ani@mesh.com' or self.password != '123456':
            list=['Credential does not match']
            raise ValidationException(list)
    
    def login(self):
        self.checkCreds()
        token = JwtHelper.generateToken(1)
        return token
