"""
Создайте программу выводящую информацию о системе вида:
Операционная система - ХХХ
Имя компьютера - ХХХ
Имя пользователя - ХХХ
"""
import os
System = os.environ.get('WINDIR')
PCNAME = os.environ.get('COMPUTERNAME')
USER = os.environ.get('USERNAME')
print(System)
print(PCNAME)
print(USER)

