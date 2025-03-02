from fastapi import HTTPException, status
from os import access
from typing import List, Optional

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import EmailStr
from backend.models.users import User
from backend.schemas.users import UserRegister, UserLogin
from backend.repositories.users import UserRepository
from backend.utils.security import verify_password, get_password_hash, create_access_token
from sqlalchemy.ext.asyncio import AsyncSession
from backend.core.config import configs





class UserService:
    def __init__(self, repo: UserRepository):
        self.user_repo = repo

    async def register(self, user_data: UserRegister) -> bool:
        return await self.user_repo.add_user(user_data)

    async def authenticate(self, email: EmailStr, password: str):
        user = await self.user_repo.find_one_or_none(email=email)
        if not user or verify_password(plain_password=password, hashed_password=user.password) is False:
            return None
        return user


    async def login(self, credential: UserLogin) -> Optional[str]:
        # Используем authenticate_user для проверки email и пароля
        user = await self.authenticate(email=credential.email, password=credential.password)
        if not user:
            return None

        access_token = create_access_token(
            data={"sub": user.email},
        )
        return access_token




    async def get_current_user(self, token: str) -> User:
        print(token)
        payload = jwt.decode(token, configs.SECRET_KEY, algorithms=[configs.ALGORITHM])
        email: str = payload.get("sub")

        user = await self.user_repo.find_one_or_none(email=email)
        return user



