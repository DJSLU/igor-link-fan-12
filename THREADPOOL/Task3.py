"""
Создайте функцию которая из файла Names.txt берет имена, превращает его в путь до файла и помещает в очередь.
Создайте функцию которая создает txt файл  по пути из очереди.
Запустите все в разных потоках.
"""
import queue
import threading

def read_names_file(queue):
    with open('Names.txt', 'r') as f:
        for line in f:
            file_path = line.strip() + '.txt'
            queue.put(file_path)
def create_files(queue):
    while not queue.empty():
        file_path =queue.get()
        with open(file_path,'w') as f:
            f.write('коректно'+ file_path)

if __name__ == '__main__':
    file_paths_queue = queue.Queue()
    read_names_thread = [threading.Thread(target=read_names_file, args=())]
    create_files_threads =[threading.Thread(target=create_files,args=())for _ in range(5)]

    read_names_thread.start()
    for t in create_files_threads:
         t.start()

    read_names_thread.join()
    for a in create_files_threads:
         a.join()

print('Завершение программы')







