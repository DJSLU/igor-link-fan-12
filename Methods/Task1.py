"""
Создайте класс Person у которого будут свойства name и age.
Добавьте метод экземпляра который выводит информацию о человеке.
Создайте метод класса который генерирует новый объект класса
который ставить возраст человека: сегодняшний год - год который передают в метод.
(подсказка: тут можно использовать метод today().year класса date из модуля datetime)
Создайте статический метод который проверяет является ли совершеннолетним человек возраст которого передается в метод.
"""


from datetime import date

class Person:
    def __init__(self, name):
        self.name = name
    def printinfo(self):
        return self.name

    def classmethod(cls, year_birth):
        age = (date.today().year - year_birth)
        return age

    def staticmethod(year_birth):
        age = (date.today().year - year_birth)
        if age in range(1, 17):
            return 'Несовершеннолетний'
        else:
            return 'Совершеннолетний'


a = Person('Emmanuil')
print(a.printinfo(), a.classmethod(2000), a.staticmethod(2008))