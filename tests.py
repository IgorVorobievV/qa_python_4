import pytest

from main import BooksCollector

@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()

    return collector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books_list_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_same_books_no_duplicates_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['', '01234567890123456789012345678901234567890', '012345678901234567890123456789012345678901'])
    def test_add_new_book_incorrect_name_no_addition(self, collector, name):
        collector.add_new_book(name)

        assert not name in collector.get_books_genre()

    def test_set_book_genre_add_genre_genre_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        assert collector.get_books_genre()['Гордость и предубеждение и зомби'] == 'Фантастика'

    def test_set_book_genre_add_missing_genre_no_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Драма')

        assert collector.get_books_genre()['Гордость и предубеждение и зомби'] == ''

    def test_get_book_genre_book_with_genre_get_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_book_genre_book_without_genre_no_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_get_books_with_specific_genre_available_genre_get_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
        
        collector.add_new_book('Гаргантюа и Пантагрюэль')
        collector.set_book_genre('Гаргантюа и Пантагрюэль', 'Комедии')

        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    @pytest.mark.parametrize('genre', ['', 'Драма', 'Ужасы'])
    def test_get_books_with_specific_invalid_genre_no_books(self, genre, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
           
        collector.add_new_book('Гаргантюа и Пантагрюэль')
        collector.set_book_genre('Гаргантюа и Пантагрюэль', 'Комедии')

        assert not collector.get_books_with_specific_genre(genre)

    def test_get_books_for_children_available_genre_get_books(self,collector):
        collector.add_new_book('Гаргантюа и Пантагрюэль')
        collector.set_book_genre('Гаргантюа и Пантагрюэль', 'Комедии')

        collector.add_new_book('Кто сказал мяу?')
        collector.set_book_genre('Кто сказал мяу?', 'Детективы')

        collector.add_new_book('Крокодил')
        collector.set_book_genre('Крокодил', 'Ужасы')

        assert len(collector.get_books_for_children()) == 1
    
    def test_get_books_for_children_missing_genre_no_books(self, collector):
        collector.add_new_book('Кто сказал мяу?')
        collector.set_book_genre('Кто сказал мяу?', 'Детективы')

        collector.add_new_book('Крокодил')
        collector.set_book_genre('Крокодил', 'Ужасы')

        assert not collector.get_books_for_children()

    def test_add_book_in_favorites_add_two_favorites_favorites_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_delete_favorite_no_favorite(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert not collector.get_list_of_favorites_books()