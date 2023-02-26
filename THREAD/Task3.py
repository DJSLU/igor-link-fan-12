"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
import threading
import time

def print_message():
    while True:
        print("Введите быстрее")
        time.sleep(3)


thread = threading.Thread(target=print_message)
thread.daemon = True
thread.start()


code = input("Введите код от бомбы: ")
if code == "монстр":
    print("Бомба разминирована")
else:
    print("Вы взорвались")