"Логика для хеширования паролей, JWT-токенов"


from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from backend.core.config import  configs

# Настройка хеширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Создание JWT-токена
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=configs.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, configs.SECRET_KEY, algorithm=configs.ALGORITHM)
    return encoded_jwt

# Проверка JWT-токена
def decode_access_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, configs.SECRET_KEY, algorithms=[configs.ALGORITHM])
        return payload
    except JWTError:
        return None