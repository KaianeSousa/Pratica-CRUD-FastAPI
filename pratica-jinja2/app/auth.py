import jwt
import datetime
from config import settings
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash(senha: str) -> str:
    """ Gera um hash seguro para a senha. """
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash_senha: str) -> bool:
    """ Verifica se a senha corresponde ao hash. """
    return pwd_context.verify(senha, hash_senha)

def gerar_token(dados: dict) -> str:
    """ Gera um JWT válido por um determinado tempo. """
    expira = datetime.datetime.utcnow() + datetime.timedelta(seconds=settings.JWT_EXPIRATION_DELTA)
    payload = {**dados, "exp": expira}
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

def validar_token(token: str):
    """ Valida um JWT e retorna os dados do usuário. """
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        return {"erro": "Token expirado"}
    except jwt.InvalidTokenError:
        return {"erro": "Token inválido"}
