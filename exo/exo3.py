# def calculatrice():

#     operation = input("Choisissez une opération (addition, multiplication, soustraction, division) : ")
    
#     if operation not in ['addition', 'multiplication', 'soustraction', 'division']:
#         print("Opération non valide.")
#         return
    
#     nombre1 = float(input("Entrez le premier nombre : "))
#     nombre2 = float(input("Entrez le deuxième nombre : "))

#     if operation == 'addition':
#         resultat = nombre1 + nombre2
#     elif operation == 'multiplication':
#         resultat = nombre1 * nombre2
#     elif operation == 'soustraction':
#         resultat = nombre1 - nombre2
#     elif operation == 'division':
#         if nombre2 != 0:
#             resultat = nombre1 / nombre2
#         else:
#             print("Division par zéro impossible.")
#             return

#     print(f"Résultat de l'opération {operation} : {resultat}")

# calculatrice()


# Avec eval ( donc n'importe quel expression mathématique ) 

def calculatrice():
    expression = input("Entrez une expression mathématique : ")
    
    try:
        resultat = eval(expression)
        print(f"Résultat de l'expression : {resultat}")
        
    except Exception as e:
        print(f"Erreur lors de l'évaluation de l'expression : {e}")





calculatrice()