"""
Напишите скрипт который в качестве параметра из командной строки принимает имя файла. Читает команды в этом файле и выполняет их
Протестируйте скрипт на файле comands.txt
"""
import sys

if len(sys.argv) < 2:
    print("Usage: python script_name.py filename")
else:
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        for line in file:

            result = eval(line.strip())
            print(result)
