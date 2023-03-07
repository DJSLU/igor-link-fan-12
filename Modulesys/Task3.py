"""
Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл где имя файла второй аргумент.
"""
import sys

if len(sys.argv) < 3:
    print("Usage: python script_name.py text_to_write filename")
else:
    text_to_write = sys.argv[1]
    filename = sys.argv[2]
    with open(filename, 'w') as file:
        file.write(text_to_write)
        print(f"{text_to_write} has been written to {filename}")
