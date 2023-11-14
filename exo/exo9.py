import random

liste_elements = [random.randint(1, 10) for _ in range(10)]

liste_carres = [x**2 for x in liste_elements]

print("Liste d'éléments aléatoires :", liste_elements)
print("Liste des carrés :", liste_carres)