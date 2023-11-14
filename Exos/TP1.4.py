import random

nombres = [random.randint(1, 100) for _ in range(10)]

maximum = nombres[0]
minimum = nombres[0]
total = 0

for nombre in nombres:
    if nombre > maximum:
        maximum = nombre
    if nombre < minimum:
        minimum = nombre
    total += nombre

if nombres:
    moyenne = total / len(nombres)
else:
    moyenne = 0

print(f"Liste de nombres : {nombres}")
print(f"Maximum : {maximum}")
print(f"Minimum : {minimum}")
print(f"Moyenne : {moyenne}")