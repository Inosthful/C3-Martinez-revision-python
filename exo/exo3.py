nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

# Effectuer les opérations
addition = nombre1 + nombre2
soustraction = nombre1 - nombre2
multiplication = nombre1 * nombre2

# Vérifier si le deuxième nombre est différent de zéro avant de faire la division
if nombre2 != 0:
    division = nombre1 / nombre2
else:
    division = "Division par zéro impossible"

# Afficher les résultats
print(f"Addition : {addition}")
print(f"Soustraction : {soustraction}")
print(f"Multiplication : {multiplication}")
print(f"Division : {division}")