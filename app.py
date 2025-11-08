# 1
sonlar = [1, 2, 3, 4, 5]

kvadratlar = list(map(lambda x: x**2, sonlar))

print(kvadratlar)


# 2
sonlar = [-3, -1, 0, 2, 4, 5]

musbat = list(filter(lambda x: x > 0, sonlar))

ikkilangan = list(map(lambda x: x * 2, musbat))

print(ikkilangan)


# 3
satrlar = input("Satrlarni vergul bilan kiriting: ").split(',')

katta = list(map(lambda s: s.upper(), satrlar))

print(katta)


# 4
sonlar = [3, 4, 6, 8, 9, 12, 15]

bolinadigan = list(filter(lambda x: x % 3 == 0, sonlar))

print(bolinadigan)


# 5
import math

a, b = 24, 36

ebob = (lambda x, y: math.gcd(x, y))(a, b)

print(ebob)


