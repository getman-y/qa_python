import pytest

from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book', ['НАСТЕНЬКА', 'НастеньКа', 'настенька'])
    def test_add_new_book_add_identical_books_with_different_letter_case(self, book):
        collector = BooksCollector()

        collector.add_new_book('Настенька')
        collector.add_new_book(book)

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('genre', ['Скандинуар', 'Документальное кино', 'Артхаус'])
    def test_set_book_genre_set_non_existent_genre(self, genre):
        collector = BooksCollector()
        name = 'Скугга-Бальдур'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.books_genre.get(name) == ''

    @pytest.mark.parametrize('book', ['Машенька', 'Подвиг', 'Камера обскура'])
    def test_get_book_genre_get_genre_of_non_existent_book(self, book):
        collector = BooksCollector()

        assert collector.get_book_genre(book) is None

    @pytest.mark.parametrize('genre', ['Скандинуар', 'Документальное кино', 'Артхаус'])
    def test_get_books_with_specific_genre_get_books_with_non_existent_genre(self, genre):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre(collector.get_books_with_specific_genre(genre)) == []

    def test_get_books_genre_get_empty_dictionary(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    def test_get_books_for_children_check_banned_genre_are_not_on_the_list(self):
        collector = BooksCollector()
        genre = "Артхаус"
        collector.genre_age_rating.append(genre)

        assert genre not in collector.get_books_for_children()

    @pytest.mark.parametrize('name', ['Котлован', 'Сало', 'Левиафан'])
    def test_add_book_in_favorites_add_already_favorite_book(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.favorites.append(name)
        collector.add_book_in_favorites(name)

        assert len(collector.favorites) == len(set(collector.favorites))

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        name = 'Скугга-Бальдур'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites

    def test_get_list_of_favorites_books_get_not_empty_list(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
