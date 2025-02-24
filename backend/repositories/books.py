from typing import List

from backend.schemas.books import Book


class BookRepository:

    def get_books(self) -> List[Book]:
        ...

    def create_book(self) -> Book:
        ...