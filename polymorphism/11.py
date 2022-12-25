"""
Создать базовый класс ОЛИМПИАДНЫЕ ЗАДАНИЯ (данные об участнике, количество тестовых примеров,
количество пройденных тестов).
Создать производные классы ЗАДАНИЯ «ВСЕ ИЛИ НИЧЕГО»
(задается максимальное количество баллов за задание (даются только когда все тесты пройдены)
и ЗАДАНИЯ «ЧЕМ БЫСТРЕЕ, ТЕМ ЛУЧШЕ» (задается время участника на решение,
лучшее время всех участников, максимальное количество баллов за задание,
процент снижения балла в минуту отставания от лучшего времени).
Для заданных примеров задач, которые решали участники,
упорядочить участников по росту набранных баллов и определить суммарное количество баллов,
набранных заданным участником олимпиады.
Для проверки использовать действия над списком,
в котором разместить объекты разных производных классов.
"""


class Задания:
    def __init__(self, name, completed, max_score):
        self.name = name
        self.completed = completed
        self.max_score = max_score

class Всёилиничего(Задания):
    def __init__(self, name, completed, max_score):
     super().__init__(name, completed, max_score)

class Чембыстреетемлучше(Задания):
    def __init__(self, name, completed, max_score, time_to_solve, score_for_task, percent, time_of_participant):
     super().__init__(name, completed, max_score)
     self.time_to_solve = time_to_solve
     self.score_for_task = score_for_task
     self.percent = percent
     self.time_of_participant = time_of_participant

class Участник:
  def __init__(self, name, tasks, total):
    self.name = name
    self.tasks = tasks
    self.total = total

  def Окончательный_счёт(self):
       for i in self.tasks:
            if i.completed and isinstance(i,Всёилиничего):
                self.total += i.max_score
            if i.completed and isinstance(i,Чембыстреетемлучше):
                self.total += i.score_for_task

def проверка_всего_времени(участники):
    all_time = []
    for i in участники:
                 for j in i.tasks:
                  if isinstance(j, Чембыстреетемлучше) and j.completed:
                                all_time.append(j.время_участников)
                 return min(all_time)


def установлеие_счёта_Чесбыстретемлучше(участнтки):
    min_ = проверка_всего_времени(участнтки)
    for p in участнтки:
        for t in p.задания:
                if isinstance(t, Чембыстреетемлучше):
                    if t.completed and t.время_участников <= t.time_to_solve:
                        if t.время_участников == min_:
                            t.очки_зазадания = t.max_score

                        else:
                            t.очки_зазадания = t.max_score - (t.max_score * t.percent / 100) * (
                                        t.время_участников - min_)

                    else:
                        t.очки_зазадания = 0








