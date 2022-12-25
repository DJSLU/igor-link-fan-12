"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: ***
"""
import json

task = ["Alina",27,["Japan","Russia"]]

s = ['name', 'age', 'countries']
def task2(task):

    obj = {}
    for i in range(len(task)):
        obj[s[i]] = task[i]
    encoded = json.dumps(obj, indent=4)

    with open('ryabinina_2.json', 'w+') as f:
        f.write(encoded)


task2(task)




