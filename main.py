n = 12345678  # Пример числа
a = n // 10000000 # целочис деление
b = (n // 1000000) % 10
c = (n // 100000) % 10
d = (n // 10000) % 10
e = (n // 1000) % 10
f = (n // 100) % 10
g = (n // 10) % 10
h = n % 10

sum = a + b + c + d + e + f + g + h #сумма всеех эл-тов
print(sum)
