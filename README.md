#Список реализованных тестов:
##test_add_new_book_add_two_books 
добавление двух книг
##test_add_new_book_negative_add_same_books
негативная проверка повторного добаления книги
##test_add_new_book_negative_input
негативная проверка добаления книги с невалидным именем (пустое значение, 41 символ, 42 символа) 
##test_set_book_genre_add_genre 
добавление жанра
##test_set_book_genre_negative_genre 
негативная проверка добавления жанра не из утвержденного списка
##test_get_book_genre_get_genre 
вывод жанра книги по имени
##test_get_books_with_specific_genre_specified_genre 
вывод списка книг по жанру
##test_get_books_with_specific_genre_negative_genre 
негативная проверка вывод списка книг с невалидным жанром (пустое значение, отсутствует в списке жанров, отсутствует в списке книг)
##test_get_books_for_children_get_books 
вывод списка книг, подходящих детям
##test_add_book_in_favorites_add_two_books
добавление двух книг в Избранное
##test_delete_book_from_favorites_delete_book
удаление книги из Избранного