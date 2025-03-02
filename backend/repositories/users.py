

from backend.models.users import User
from backend.schemas.users import UserRegister
from backend.utils.security import get_password_hash

from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def find_one_or_none(self, email: str) -> User:
        query = select(User).where(User.email == email)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def add_user(self, user: UserRegister) -> bool:
        existing_user = await self.find_one_or_none(user.email)
        if existing_user:
            return False
        db_user = User(
            email=user.email,
            password=get_password_hash(user.password),
            phone_number=user.phone_number,
            first_name=user.first_name,
            last_name=user.last_name,
            is_admin=user.is_admin
        )
        self.session.add(db_user)
        await self.session.commit()
        return True  # Пользователь успешно добавлен

