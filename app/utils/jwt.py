import jwt
import datetime
from fastapi import HTTPException

class AuthService:
    SECRET_KEY = "jmb28()"
    ALGORITHM = "HS256"

    @staticmethod
    def create_token(user):
        payload = {
            'id': user['id'],
            'nombre': user['nombre'],
            'apellido': user['apellido'],
            'rol': user['rol'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expira en 1 hora
        }
        token = jwt.encode(payload, AuthService.SECRET_KEY, algorithm=AuthService.ALGORITHM)
        return token

    @staticmethod
    def verify_token(token: str):
        try:
            payload = jwt.decode(token, AuthService.SECRET_KEY, algorithms=[AuthService.ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expirado")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Token inválido")
