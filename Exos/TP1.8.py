eleves = {
    'Brown Alicia': 92,
    'Doe John': 90,
    'Johnson Emily': 78,
    'Brown Alice': 92,
    'Doe Johnas': 88
}

notes_par_nom = {}
for eleve, note in eleves.items():
    nom, prenom = eleve.split()
    cle = (nom, prenom)
    if cle not in notes_par_nom:
        notes_par_nom[cle] = []
    notes_par_nom[cle].append(note)

