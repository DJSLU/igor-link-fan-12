"""
Напишите скрипт который принимает 2 аргумента - путь и имя папки. И создаем папку по указанному пути.
"""
import sys
import os

if len(sys.argv) < 3:
    print("Usage: python script_name.py path folder_name")
else:
    path = sys.argv[1]
    folder_name = sys.argv[2]
    folder_path = os.path.join(path, folder_name)
    os.mkdir(folder_path)
    print(f"Folder {folder_name} has been created in {path}")
