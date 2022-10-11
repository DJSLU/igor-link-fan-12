numbers = "0139412831055230677798"
a = dict()
for i in range(10):
    a[i] = numbers.count(str(i))
print(a)