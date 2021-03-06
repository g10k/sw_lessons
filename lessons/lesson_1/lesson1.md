# Занятие 1
Знакомство с github. Язык Python. Знакомство с pip, virtualenv. Первые команды на python. Знакомство с основными типами данных, операторами Python. Обзор структуры проекта django.

```
python # мы попали в интерпретатор python >>> видим, версию 2.7.x или 3.5 на ubuntu 16.04. 
>>> exit() - выход из интерпретатора
sudo apt-get install virtualenv python-pip
mkdir lesson1
virtualenv venv_python2.7
source venv_python2.7/bin/activate # Активируем виртуальное окружение, есть shortcut virtualenvwrapper сделать это командой короче.
pip install ipython # установим в виртуальном окружении ipython
python 
```
Выполняем команды из [руководства для новичков](http://pythontutor.ru/lessons/inout_and_arithmetic_operations/)
 1. Считаем площадь треугольника
 1. функция категории числа: -1, 0, 1

Что нужно запомнить
 - Переменные динамически типизированные
 - отличия python2.7 и python3  ```from __future__ import absolute_import unicode_literals, print_function``` # Должно быть в начале файла
 - Отступы важны (tab или space, но не смешивать)

Устанавливаем django
```
source venv_python2.7/bin/activate 
(venv) ~ pip install django # Рассказать про версионирование пакетов.
pip freeze # Смотрим какие пакеты стоят в текущем виртуальном окружении 
deactivate выходим из вирт. окружения
pip freeze Смотрим что тут django нету

source venv_python2.7/bin/activate 
django-admin # Изучаем вывод команды
django-admin startproject first_project
Изучаем файлы  django проекта.

```
[Модель работы Django](http://rnevius.github.io/django_request_response_cycle.png)

### Ссылки


[Инструкция для отправки своего кода на github](https://github.com/g10k/sw_lessons/blob/master/lessons/lesson_1/install_and_commit_via_git.md)

[Инструкция](http://ru.wikihow.com/%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%82%D1%8C-Ubuntu-%D0%B2-VirtualBox)  как установить ubuntu на виртуальную машину Linux.

[Основные команды linux](http://forum.ubuntu.ru/index.php?topic=14535.15)

[Курс по git](https://githowto.com/ru)

[Отличия python 2 и 3](https://pythonworld.ru/osnovy/python2-vs-python3-razlichiya-sintaksisa.html) | [Официальные](https://docs.python.org/3.0/whatsnew/3.0.html)

[Оформление кода Python](http://pep8.ru/doc/pep8/) | [PEP8](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html)

[Вводное описание django](https://tutorial.djangogirls.org/ru/django/)

[Первый урок django на djbook](http://djbook.ru/rel1.9/intro/tutorial01.html)

[Почему важно обучать других и отвечать на вопросы](https://lh4.googleusercontent.com/_OY-yBNwZY8I/TayPMZwe68I/AAAAAAAABzI/tSXTW-fyv5k/LearningPyramid.JPG)
