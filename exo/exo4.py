import random

liste_nombres = [random.randint(1, 100) for _ in range(10)]

# Trouver le maximum, le minimum et calculer la moyenne
maximum = max(liste_nombres)
minimum = min(liste_nombres)
moyenne = sum(liste_nombres) / len(liste_nombres)

# Afficher les résultats
print(f"Liste de nombres : {liste_nombres}")
print(f"Maximum : {maximum}")
print(f"Minimum : {minimum}")
print(f"Moyenne : {moyenne}")