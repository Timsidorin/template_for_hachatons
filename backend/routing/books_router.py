from typing import List

from fastapi import APIRouter, Depends


router = APIRouter(prefix="/books", tags=["Книги"])


@router.get(
    "",
    responses={400: {"description": "Bad request"}},
    #response_model=List[Book],
    description="Получение листинга всех книг",
)

async def получение_списка_книг():
    return {"message": "return_books"}
