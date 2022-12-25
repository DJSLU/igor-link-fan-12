"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""
class Man():
    def make_sound (self):
        print('Крякает как утка')

    def clother(self):
        print('человек в пальто')


class Duck():
    def make_sound(self):
        print('Крякает')

    def clother(self):
        print('Утка в чёрных очках')

man1=Man()
duck =Duck()

for stange in (man1,duck):
    stange.make_sound()
    stange.clother()
