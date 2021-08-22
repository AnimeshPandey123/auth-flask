import jwt

class JwtHelper:
    def generateToken(email):
        return jwt.encode({"email": email}, 'test', algorithm="HS256")