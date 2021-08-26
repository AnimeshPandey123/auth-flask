import jwt
import datetime

class JwtHelper:
    def generateToken(user_id):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(payload, 'test', algorithm="HS256")