# Список реализованных тестов:
## test_add_new_book_add_two_books_list_two_books 
добавление двух книг
## test_add_new_book_add_same_books_no_duplicates_books
негативная проверка повторного добаления книги
## test_add_new_book_incorrect_name_no_addition
негативная проверка добаления книги с невалидным именем (пустое значение, 41 символ, 42 символа) 
## test_set_book_genre_add_genre_genre_added
добавление жанра
## test_set_book_genre_add_missing_genre_no_genre 
негативная проверка добавления жанра не из утвержденного списка
## test_get_book_genre_book_with_genre_get_genre 
вывод жанра книги по имени
## test_get_book_genre_book_without_genre_no_genre
негативная проверка вывода жанра книги, когда у книги нет жанра
## test_get_books_with_specific_genre_available_genre_get_books
вывод списка книг по жанру
## test_get_books_with_specific_invalid_genre_no_books 
негативная проверка вывода списка книг с невалидным жанром (пустое значение, отсутствует в списке жанров, отсутствует в списке книг)
## test_get_books_for_children_available_genre_get_books
вывод списка книг, подходящих детям
## test_get_books_for_children_missing_genre_no_books
негативная проверка вывода списка книг, подходящих детям, когда книги с возрастным рейтингом отсутствуют в списке книг для детей
## test_add_book_in_favorites_add_two_favorites_favorites_added
добавление двух книг в Избранное
## test_delete_book_from_favorites_delete_favorite_no_favorite
удаление книги из Избранного
