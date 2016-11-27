# Занятие 2
Работа в git. Простейшие задачи на python. Функции, объекты, классы.

Рассказ о git. [Основы git](https://git-scm.com/book/ru/v1/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-Git) 
[Запись изменений](https://git-scm.com/book/ru/v1/%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-Git-%D0%97%D0%B0%D0%BF%D0%B8%D1%81%D1%8C-%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B2-%D1%80%D0%B5%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B9)
Практический пример от использования git. (в pycharm это нагляднее) 20 минут
 - clone
 - 3 стадии изменения файла.
 - пушим файл в мастер. (показать, что нужно будет сливать изменения если кто-то еще запушит в master)
 - создаем ветку для себя, делаем чекаут.
 - создаем файлы, пушим  ветку.

PEP8 (Именование переменных) (10 минут)
 
Рассказ о [установке PyCharm](https://www.jetbrains.com/pycharm/download/#section=linux) (5 минут)
 - скачиваем
 - указание JAVA_HOME в файле pycharm.sh
 - запуск и создание ярлыка
 
Проверка домашних заданий.
  - упражнения
  
  - рассказ про классы: вступление из книги о "Зачем нужны классы", стр. 696.
    - классы это фабрики пораждающие экземпляры объектов;
    - доступ к атрибутам класса
    - комбинирование классов (Часто в книжках примеры про Животных, фигуры и проч. в жизни это больше метод DRY)
    - методы перезагрузки, __init__

  - области видимости
  - передача аргументов в функции
  - наиболее используемые пакеты и как их искать и устанавливать. (random, string, os, sys)
  - рассказ о ```__name__ == __main__```:
  - пример файла, решающего задачи из 1 урока.
  - программка для работы с файлами ОС (скрипт)
  - ответы на вопросы, описание часто встречаемых исключений
  
  
Рассказ о django приложении polls:
  - запуск приложения в режиме разработки.
  - написание еще одного урла
 

# Домашнее задание.

1. Функция сложения матриц. Вывод матриц по столбцам, по строкам.
1. Написать класс, которому мы задаем размерность. У него методы:
```python
class SquareMatrix(object):
    def __init__(self, size):
        self.size = size

    def create_matrix(self):
        # Создаем матрицу с использованием random , сохраняем в атрибут self._matrix и возвращаем ее
        pass

    def get_matrix(self):
        # отдаем матрицу
        pass

    def get_element(self,i,j):
        # вернуть self._matrix[i][j]
        # предусмотреть, что i,j могут быть введены больше чем размерность, тогда вернуть None
        pass

    def add_to_element(self,i,j, value):
        # Добавить self._matrix[i][j] + value
        pass

    def get_transposed_matrix(self):
        # вернуть транспонированную матрицу
        pass

    def print_hypno(self):
        # Для матрицы
        # [1, 8, 7],
        # [2, 9, 6],
        # [3, 4, 5]
        # Вывести [1,2,3,4,5,6,7,8,9]
        pass

    def print_snake(self):
        # [1, 8, 7],
        # [2, 9, 6],
        # [3, 4, 5]
        # Вывести [1, 2, 3, 4, 9, 8, 7, 6, 5]
        pass
        
    def make_improvization(self):
        # задача на импровизацию, сделайте сами что-нибудь интересное
        pass

class Matrix(object):
    # Написать матрицу, но уже не квадратную, а размерности N x M, также задавать через конструктор.
    pass
```
  
1. Установить PyCharm.
1. Скачать приложение django из репозитория, запустить его, добавить свой url. Запушить в свою ветку.