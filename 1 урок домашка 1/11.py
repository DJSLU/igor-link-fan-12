print("Введите массу в киллограмах:")
r = int(input())
print("Введите рост в сантиметрах:")
santi = int(input())
h2 = float((santi / 100) ** 2)
i = r / h2
print(round(i, 2))