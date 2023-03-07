"""
Запустите фоновый процесс который следит за сроком подписки пользователя( для примера 10 секунд) если время подписки вышло выведите надпись "Ваша подписка закончилась."
и завершите работу программы. В основной программе сыграйте с пользователем в игру "угадай число".
"""

import multiprocessing as mp
import time
import random

def subscription_time():
    time.sleep(10)
    print('Ваша подписка закончилась')
    mp.terminate()
if __name__ == '__main__':
    p = mp.Process(target=subscription_time)
    p.start()


    number =random.randint(1,100)
    guess = None
    while guess != number:
        guess = int(input('Введите число от 1 до 100'))
        if guess > number:
            print('Меньше...')
        elif guess < number:
            print('Больше...')
        else:
            print('Вы угадали')
            break

            p.terminate()
            p.join()














