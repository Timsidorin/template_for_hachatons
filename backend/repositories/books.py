from datetime import datetime
from typing import List

from backend.schemas.books import Book, Author
from backend.services import  books


class BookRepository:

    def get_books(self) -> List[Book]:


        return books

    def create_book(self) -> Book:
        ...