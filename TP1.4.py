import random

nombres = [random.randint(1, 100) for _ in range(10)]

maximum = max(nombres)
minimum = min(nombres)
moyenne = sum(nombres) / len(nombres)

print(f"Liste de nombres : {nombres}")
print(f"Maximum : {maximum}")
print(f"Minimum : {minimum}")
print(f"Moyenne : {moyenne}")