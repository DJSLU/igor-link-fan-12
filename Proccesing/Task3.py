"""
Напишите функцию которая через канал обмена возвращает количество валюты которую можно приобрести на n сумму денег при курсе 1 к 75.
Запустите функцию в отдельном процессе и отправьте в нее данные задержкой в 0.5 секунды передайте ей разное количество доступных денег.
Выводите количество валюты на экран по мере обработки данных.
"""
import multiprocessing as mp
import time

def currency_exchange(money,conn):
    rate = 75
    currency = money/rate
    conn.send(currency)

if __name__ == '__main__':
    conn,child_conn =mp.Pipe()

    p = mp.Process(target=currency_exchange, args=(child_conn, 1000))
    p.start()

    for money in [400,2500,10000]:
        time.sleep(0.5)
        conn.send(money)
        currency = conn.recv()
        print(f'На{money} сумму можно приобрести {currency} валюты')
        p.join()

