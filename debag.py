from books_sdk import get_author, get_book_by_id
print(get_author(get_book_by_id('AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM','1' )))

# Гипотеза 1: Неправильные скобки
# Способ проверки: Удалить весь код, кроме скобок, и проверить их количество и порядок
# Установленный факт: В данной функции все скобки расположены правильно
# Вывод: Гипотеза опроверглась, со скобками всё в порядке

# Гипотеза 2: Ошибка во вложенной функции
# Способ проверки: Запустить вложенную функцию отдельно от внешней
# Код для проверки: print(get_book_by_id('1', 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM'))
# Установленный факт:Вложенная функция не вызывается
# Вывод:Гипотеза опроверглась

# Гипотеза 3: Проблема в типе данных, '1' должно быть числом
# Способ проверки: Удаление кавычек
# Код для проверки:from books_sdk import get_book_by_id, get_author
#print(get_author(get_book_by_id(1, 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM')))
# Установленный факт: Функция get_book_by_id возвращает строку, а не число
# Вывод: Гипотеза опроверглась

# Гипотеза 4: Книги с номером 1 не существует
# Способ проверки:Проверить, есть результат вызову книги с id 1
# Код для проверки:from books_sdk import get_author, get_book_by_id
#print(get_author(get_book_by_id('1', 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM')))
# Установленный факт: Функция выдает ошибку токена а не id числа
# Вывод: Гипотеза опроверглась

# Гипотеза 5:Аргументы перепутаны местами
# Способ проверки: Переставиь аргументы
# Код для проверки: from books_sdk import get_author, get_book_by_id
#print(get_author(get_book_by_id('AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM','1' )))
# Установленный факт: аргементы перепутанны местами
# Вывод:Гипотеза подтвердилась
