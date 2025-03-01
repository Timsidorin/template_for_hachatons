from datetime import datetime

from sqlalchemy import Column, Integer
from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sa
from backend.core.database import *






class Book(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(sa.String(100))
    annotation: Mapped[str] = mapped_column(sa.Text)
    date_publishing: Mapped[datetime] = mapped_column(sa.DateTime)


# async def create_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


async def create_book_example():
    # Получаем сессию через генератор
    session_gen = get_async_session()


        # Получаем сессию из асинхронного генератора
    session = await session_gen.__anext__()
        # Создаем книгу
    new_book = Book(
            title="Преступление и наказание",
            annotation="Роман о нравственных терзаниях",
            date_publishing=datetime(1866, 1, 1),
        )

        # Добавляем и коммитим
    session.add(new_book)
    await session.commit()
    print("Книга успешно добавлена!")

# Запуск
if __name__ == "__main__":
    import asyncio
    asyncio.run(create_book_example())