"""
Создайте функцию которая выводит на экран все делители числа.
Создайте очередь и добавьте в нее числа.
Создайте пул потоков и запустите в пуле функцию с очередью.
"""
import queue
import concurrent.futures

def print_divisors(n):
    """Prints all divisors of the given integer n"""
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    print(f"Divisors of {n}: {divisors}")


q = queue.Queue()
q.put(12)
q.put(24)
q.put(36)


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    while not q.empty():
        n = q.get()
        executor.submit(print_divisors, n)
