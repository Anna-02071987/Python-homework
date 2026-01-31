Lesson 3 — OOP (User and Smartphone)
Описание

Домашняя работа по уроку 3.  
Цель — освоить основы объектно-ориентированного программирования (OOP) в Python.

В рамках задания реализованы классы и примеры их использования.

Реализованные классы

 User
Класс пользователя с базовыми характеристиками.

 Smartphone
Класс смартфона со следующими атрибутами:
- бренд
- модель  
- номер телефона

Также реализован метод:
- `print_info()` — вывод информации о смартфоне

 Пример использования

```python
from smartphone import Smartphone

phone1 = Smartphone("Apple", "iPhone 15", "+79990000001")
phone2 = Smartphone("Samsung", "Galaxy S23", "+79990000002")
phone3 = Smartphone("Xiaomi", "Redmi Note 12", "+79990000003")

phone1.print_info()
phone2.print_info()
phone3.print_info()
