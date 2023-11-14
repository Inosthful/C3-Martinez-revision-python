def factorielle(n):
    """Calcule la factorielle d'un nombre."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n - 1)



nombre = 5
resultat = factorielle(nombre)

print(f"La factorielle de {nombre} est {resultat}")