"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""
import queue
import threading


students_queue = queue.Queue()


def add_students():
    while True:

        surname = input("Введите фамилию студента или 'off' для завершения: ")
        if surname == "off":

            break
        else:

            students_queue.put(surname)


def dismiss_students():
    while True:

        surname = students_queue.get()

        print("Студент {} отчислен".format(surname))

        students_queue.task_done()


students_queue.put("Пыхтин")
students_queue.put("Суранов")


add_thread = threading.Thread(target=add_students)
dismiss_thread = threading.Thread(target=dismiss_students)

add_thread.start()
dismiss_thread.start()


add_thread.join()
dismiss_thread.join()


print("Программа завершена")
