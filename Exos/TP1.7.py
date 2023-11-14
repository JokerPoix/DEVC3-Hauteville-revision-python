with open('TP1.7texte.txt', 'r') as file:
    contenu = file.read()
    mots = contenu.split()
    nombre_mots = len(mots)

with open('TP1.7resultat.txt', 'w') as output_file:
    output_file.write(f"Le nombre de mots dans le fichier texte est : {nombre_mots}")