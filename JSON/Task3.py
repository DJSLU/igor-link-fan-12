"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: [
{
name:***
time:***
cities:***
}
]
"""

import json

task = ["Alina",27,["Japan","Russia"],(26,1),["Itinomia","Tokio",'Kioto',"Nagoya","Yakagama"]]
arr = ['name', 'age', 'countries', 'name', 'time', 'cities']

obj = {}
for i in range(2):
    obj[arr[i]] = task[i]

obj[arr[2]] = {}

k = 0
for i in range(3, 6):
    obj[arr[2]][arr[i]] = task[i - 1]



print(obj)
encoded = json.dumps(obj, indent=4)

with open('emmanuil.json', 'w+') as f:
    f.write(encoded)