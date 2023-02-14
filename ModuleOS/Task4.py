""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""

import os
os.mkdir(r'D:\task4')
os.chdir(r'D:\task4')
with open('answer.txt', 'w') as f:
    f.write('я выполнил задани')