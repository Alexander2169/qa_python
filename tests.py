import pytest

from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_without_genre_true(self, books_collector):
        book_name = "Новая книга"
        books_collector.add_new_book(book_name)
        assert len(books_collector.books_genre) == 1

    def test_add_new_book_the_same_book_can_be_added_only_once_true(self, books_collector):
        book_name = "Одна и та же книга"
        books_collector.add_new_book(book_name)
        books_collector.add_new_book(book_name)
        assert len(books_collector.books_genre) == 1

    def test_add_new_book_name_more_than_40_characters_false(self, books_collector):
        invalid_name = "Сорок один Сорок один Сорок один Сорок один"
        books_collector.add_new_book(invalid_name)
        assert len(books_collector.books_genre) == 0











