from datetime import datetime
from typing import List

from backend.schemas.books import Book, Author
from backend.services import  books


class BookRepository:

    def get_books(self) -> List[Book]:


        author1 = Author(
            first_name="Джордж",
            last_name="Оруэлл",
            date_birth=datetime(1903, 6, 25),
            biography="Британский писатель и журналист, автор антиутопий"
        )

        author2 = Author(
            first_name="Фёдор",
            last_name="Достоевский",
            date_birth=datetime(1821, 11, 11),
            biography="Русский писатель, философ и мыслитель"
        )


        books = [
            Book(
                title="1984",
                annotation="Антиутопия о тоталитарном обществе и контроле над разумом",
                date_publishing=datetime(1949, 6, 8),
                author=author1
            ),
            Book(
                title="Преступление и наказание",
                annotation="Роман о моральной дилемме и искуплении",
                date_publishing=datetime(1866, 1, 1),
                author=author2
            )
        ]

        return books

    def create_book(self) -> Book:
        ...