"""
Создайте программу создающую папку target внутри которой еще 10 папок имена которых цифры от 1 до 10
"""
import os
os.mkdir(r"D:\target")
os.makedirs(r"D:\target\1\2\3\4\5\6\7\8\9\10")
print(os.mkdir())
print(os.makedirs())