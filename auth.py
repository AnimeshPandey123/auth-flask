from flask import jsonify
import jwt

class auth:
    def __init__(self,email, password):
        self.email = email
        self.password = password
        self.key = "secret"

    def checkCreds(self):
        if self.email == 'ani@mesh.com' and self.password == '123456':
            return True
        return False
    
    def login(self):
        if self.checkCreds() == False:
            return jsonify({'message': "Invalid Credentials"})
        token = self.generateToken()

    def generateToken(self):
        return jwt.encode({"email": self.email}, self.key, algorithm="HS256")
