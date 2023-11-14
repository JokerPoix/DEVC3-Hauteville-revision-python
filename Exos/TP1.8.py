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

meilleure_note = max(note for notes in notes_par_nom.values() for note in notes)

meilleurs_eleves = {eleve: notes for eleve, notes in notes_par_nom.items() if max(notes) == meilleure_note}

meilleurs_eleves_tries = dict(sorted(meilleurs_eleves.items(), key=lambda x: (-max(x[1]), x[0][0], x[0][1])))


