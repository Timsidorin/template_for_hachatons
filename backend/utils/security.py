from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from backend.core.config import get_auth_data

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(to_encode, auth_data['secret_key'], algorithm=auth_data['algorithm'])
    return encode_jwt


def decode_access_token(token: str) -> Optional[dict]:
    """
    Декодирует и проверяет JWT токен.

    Args:
        token: JWT токен для проверки

    Returns:
        Optional[dict]: Декодированные данные токена или None при ошибке
    """
    try:
        payload = jwt.decode(token, configs.SECRET_KEY, algorithms=[configs.ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        print("Токен истек")
        return None
    except jwt.InvalidTokenError:
        print("Недействительный токен")
        return None
    except Exception as e:
        print(f"Ошибка при декодировании токена: {str(e)}")
        return None