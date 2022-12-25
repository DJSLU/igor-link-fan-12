"""
Выведите из файла character.json Имя персонажа,родную планету и список эпизодов в которых он появлялся.
"""


import json

with open("character.json", "r") as dead:
    data = json.load(dead)
def char(name,planet):
    print(
        f"Имя персонажа - {name}, родная планета: {planet} \n эпизоды: ")
    for i in data["episode"]:
        print(f"- {i}")

name = data["name"]
planet = data["origin"]["name"]

char(name, planet)