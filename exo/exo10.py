def tri_insertion(liste):

    for i in range(len(liste)):
        valeur_a_inserer = liste[i]
        j = i - 1

        while j >= 0 and valeur_a_inserer < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1

        liste[j + 1] = valeur_a_inserer

    return liste

# Exemple d'utilisation
ma_liste = [12, 4, 5, 6, 7, 3, 1, 15,2]
liste_triee = tri_insertion(ma_liste)
print("Liste triée par insertion :", liste_triee)