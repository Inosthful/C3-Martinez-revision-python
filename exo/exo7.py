notes_eleves = {
    'Lucas Smith': 24,
    'Zlatan Ibramovic': 10,
    'Syouli Prime': 80,
    'Faker Goat': 98,
    'Caliste LEC': 95,
    'Alex Martin': 100,
    'Elon Musk': 100,
    
        
    
}

note_maximale = max(notes_eleves.values())

# Trouver les élèves avec la meilleure note
meilleurs_eleves = [eleve for eleve, note in notes_eleves.items() if note == note_maximale]


meilleur_eleve = meilleurs_eleves[0]
print(f"L'élève avec la meilleure note est : {meilleur_eleve} avec la note {note_maximale}")
