import pytest

from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_true(self, books_collector):
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

    def test_set_book_genre_true(self, books_collector):
        books_collector.add_new_book("Космические пираты")
        books_collector.set_book_genre("Космические пираты", "Фантастика")
        assert books_collector.books_genre["Космические пираты"] == "Фантастика"

    def test_get_book_genre_true(self, books_collector):
        books_collector.add_new_book("Космические пираты")
        books_collector.set_book_genre("Космические пираты", "Фантастика")
        assert books_collector.get_book_genre("Космические пираты") == "Фантастика"
        assert books_collector.get_book_genre("Нет книги") is None

    @pytest.mark.parametrize(
        "genre, name_book",
        [
            ("Фантастика", ["Космические пираты"]),
            ("Мультфильмы", ["Колобок"]),
            ("Комедии", ["Приключения Шурика"])
        ]
    )
    def test_get_books_with_specific_genre_true(self, books_collector, genre, name_book):
        books_collector.add_new_book("Космические пираты")
        books_collector.add_new_book("Колобок")
        books_collector.add_new_book("Приключения Шурика")

        books_collector.set_book_genre("Космические пираты", "Фантастика")
        books_collector.set_book_genre("Колобок", "Мультфильмы")
        books_collector.set_book_genre("Приключения Шурика", "Комедии")

        books = books_collector.get_books_with_specific_genre(genre)
        assert sorted(books) == sorted(name_book)

    def test_get_books_genre_true(self, books_collector):
        books_collector.add_new_book("Космические пираты")
        books_collector.add_new_book("Колобок")

        books_collector.set_book_genre("Космические пираты", "Фантастика")
        books_collector.set_book_genre("Колобок", "Мультфильмы")

        assert books_collector.get_books_genre() == {"Космические пираты":"Фантастика", "Колобок":"Мультфильмы"}

    def tests_get_books_for_children_true(self, books_collector):
        books_collector.add_new_book("Вий")
        books_collector.add_new_book("Колобок")
        books_collector.add_new_book("Приключения Шурика")

        books_collector.set_book_genre("Вий", "Ужасы")
        books_collector.set_book_genre("Колобок", "Мультфильмы")
        books_collector.set_book_genre("Приключения Шурика", "Комедии")

        assert sorted(books_collector.get_books_for_children()) == sorted(["Колобок", "Приключения Шурика"])

    def tests_add_book_in_favorites_true(self, books_collector):
        books_collector.add_new_book("Приключения Шурика")
        books_collector.add_book_in_favorites("Приключения Шурика")
        assert "Приключения Шурика" in books_collector.favorites

    def tests_delete_book_from_favorites_true(self, books_collector):
        books_collector.add_new_book("Приключения Шурика")
        books_collector.add_book_in_favorites("Приключения Шурика")
        books_collector.delete_book_from_favorites("Приключения Шурика")
        assert "Приключения Шурика" not in books_collector.favorites

    def tests_get_list_of_favorites_books_true(self, books_collector):
        books_collector.add_new_book("Космические пираты")
        books_collector.add_new_book("Колобок")

        books_collector.add_book_in_favorites("Космические пираты")
        books_collector.add_book_in_favorites("Колобок")

        assert list(books_collector.get_list_of_favorites_books())









