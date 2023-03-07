+"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 1000000
"""
import multiprocessing

def sum_even_numbers(start, end, result_queue):
    """Считает сумму четных чисел в диапазоне от start до end и добавляет результат в очередь result_queue"""
    result = 0
    for i in range(start, end+1):
        if i % 2 == 0:
            result += i
    result_queue.put(result)

def sum_odd_numbers(start, end, result_queue):
    """Считает сумму нечетных чисел в диапазоне от start до end и добавляет результат в очередь result_queue"""
    result = 0
    for i in range(start, end+1):
        if i % 2 != 0:
            result += i
    result_queue.put(result)

if __name__ == '__main__':

    result_queue = multiprocessing.Queue()


    even_process = multiprocessing.Process(target=sum_even_numbers, args=(1, 1000000, result_queue))
    odd_process = multiprocessing.Process(target=sum_odd_numbers, args=(1, 1000000, result_queue))


    even_process.start()
    odd_process.start()


    even_process.join()
    odd_process.join()


    even_sum = result_queue.get()
    odd_sum = result_queue.get()


    print("Сумма четных чисел от 1 до 1000000:", even_sum)
    print("Сумма нечетных чисел от 1 до 1000000:", odd_sum)
