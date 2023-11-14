import random

liste_nombres = [random.randint(1, 100) for _ in range(10)]


maximum = max(liste_nombres)
minimum = min(liste_nombres)
moyenne = sum(liste_nombres) / len(liste_nombres)


print(f"Liste de nombres : {liste_nombres}")
print(f"Maximum : {maximum}")
print(f"Minimum : {minimum}")
print(f"Moyenne : {moyenne}")