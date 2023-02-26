"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""
import threading

def reminder():
    text = input("Введите напоминание: ")
    time = int(input("Через сколько секунд напомнить? "))
    timer = threading.Timer(time, lambda: print(f"Напоминание: {text}"))
    timer.start()

reminder_thread = threading.Thread(target=reminder)
reminder_thread.start()


time.sleep(10)

print("Программа завершается")