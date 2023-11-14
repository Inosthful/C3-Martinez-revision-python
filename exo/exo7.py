def countWords(test):
    try:
       
        with open(test, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            nombre_mots = len(contenu.split())

        return nombre_mots

    except FileNotFoundError:
        print(f"Le fichier '{test}' n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None
    
def writeResult(fichierResultat, nbr):
    try:
        with open(fichierResultat, 'w', encoding='utf-8') as fichier_sortie:
            fichier_sortie.write(f"Nombre de mots dans le fichier : {nbr}")

        print(f"Résultat écrit dans le fichier '{fichierResultat}'.")

    except Exception as e:
        print(f"Une erreur s'est produite lors de l'écriture du résultat : {e}")


test = 'text.txt'
test2 = 'text2.txt'
nombre_mots = countWords(test)

if nombre_mots is not None:
    writeResult(test2, nombre_mots)    