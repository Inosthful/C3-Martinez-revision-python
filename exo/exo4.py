import random

liste_nombres = [random.randint(1, 100) for _ in range(10)]

maximum = liste_nombres[0]
minimum = liste_nombres[0]

somme = 0
compteur = 0

# Parcourir la liste pour trouver le maximum, le minimum et calculer la somme
for nombre in liste_nombres:
    if nombre > maximum:
        maximum = nombre
    elif nombre < minimum:
        minimum = nombre
    somme += nombre
    compteur += 1

# Calculer la moyenne
moyenne = somme / compteur

print(f"Liste de nombres : {liste_nombres}")
print(f"Maximum : {maximum}")
print(f"Minimum : {minimum}")
print(f"Moyenne : {moyenne}")