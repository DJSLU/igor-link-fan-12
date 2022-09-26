Amount = int(input())
Time = int(input())
if (Time >= 10) and (Time <= 12):
    print(Amount/2)
elif (Time >= 20) and (Time <= 22):
    print(Amount/4)
elif ((Time >= 8) and (Time < 10)) or ((Time > 12) and (Time < 20)):
    print(Amount)
else:
    print('Мы не работаем')