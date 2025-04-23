from math import sqrt
print("Ievadi skaitlus")
a = int(input())
b = int(input())
c = int(input())
d = b * b - 4 * a * c
if d < 0:
    print("Sakņu nav.")
if d == 0:
    x = -b / (2* a)
    print("Viena sakne.", x)
if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print("Divas saknes.", x1, x2 )