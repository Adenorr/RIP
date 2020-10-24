from operator import itemgetter
import re

class Book:
    """Книга"""
    def __init__(self, id, name, size, lib_id):
        self.id = id
        self.name = name
        self.size = size
        self.lib_id = lib_id

class Lib:
    """Библиотека"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class BookLib:
    """Книги в библиотеке"""
    def __init__(self, lib_id, book_id):
        self.lib_id = lib_id
        self.book_id = book_id

# Библиотеки
libs = [
   Lib(1, 'Российская государственная библиотека'),
   Lib(2, 'Научная библиотека им. Ушакова'),
   Lib(3, 'Академическая библиотека Академии наук'),
   Lib(22, 'Библиотека-читальня им. Тургенева'),

   Lib(11, 'Самарская библиотека искусств'),
   Lib(33, 'Политехническая библиотека'),
]

# Книги
books = [
    Book(1, 'Достоевский Ф. Бесы', 309, 1),
    Book(2, 'Шрёдингер Э. Что такое жизнь с точки зрения физика?', 142, 2),
    Book(3, 'Юнг К. Красная Книга', 280, 3),
    Book(4, 'Линор Горалик. Все, способные дышать', 795, 3),
    Book(5, 'Атанасян Л. С. Геометрия Лобачевского', 89, 3),
    Book(5, 'Садбери А. Квантовая механика и физика элементарных задач', 201, 22),
    Book(5, 'Платонов А. П. В прекрасном и яростном мире', 27, 22),
]

books_libs = [
    BookLib(1,1),
    BookLib(2,2),
    BookLib(3,3),
    BookLib(3,4),
    BookLib(3,5),
    BookLib(22,2),

    BookLib(11,1),
    BookLib(33,3),
    BookLib(33,4),
    BookLib(33,5),
]

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим 
    one_to_many = [(f.name, f.size, d.name)
        for d in libs
        for f in books
        if f.lib_id==d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, fd.lib_id, fd.book_id)
        for d in libs
        for fd in books_libs
        if d.id==fd.lib_id]

    many_to_many = [(f.name, f.size, lib_name)
        for lib_name, lib_id, book_id in many_to_many_temp
        for f in books if f.id==book_id]

    print('Задание А1')
    res_11 = {}
    selected_libs = [one_lib[2] for one_lib in one_to_many if one_lib[2].startswith('а') or one_lib[2].startswith('А')]
    for lib_name in selected_libs:
        books_in_lib = [(one_book[0],one_book[1]) for one_book in one_to_many if one_book[2]==lib_name]
        res_11.update({lib_name:books_in_lib})
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    for d in libs:
        d_books = list(filter(lambda i: i[2]==d.name, one_to_many))
        if len(d_books) > 0:
            d_sizes = [size for _,size,_ in d_books]
            d_size_max = max(d_sizes)
            res_12_unsorted.append((d.name, d_size_max))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = sorted(many_to_many, key = itemgetter(2))
    print(res_13)

if __name__ == '__main__':
    main()

