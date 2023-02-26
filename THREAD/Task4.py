"""
Создайте функцию которая принимает путь до файла из папки files и меняет в нем "ids" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""
import os
import glob
import re
import threading
import time

def replace_ids_in_file(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    updated_content = re.sub('ids', 'id', content)
    with open(filepath, 'w') as file:
        file.write(updated_content)

if __name__ == '__main__':
    start_time = time.time()
    folder_path = 'files/'
    file_extension = '*.txt'
    files = glob.glob(os.path.join(folder_path, file_extension))
    threads = []
    for file in files:
        t = threading.Thread(target=replace_ids_in_file, args=(file,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    print(f"Время выполнения программы: {end_time - start_time} секунд")
