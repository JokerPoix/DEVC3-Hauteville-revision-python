def tri_insertion(liste):
    for i in range(1, len(liste)):
        valeur_actuelle = liste[i]
        position = i

        while position > 0 and liste[position - 1] > valeur_actuelle:
            liste[position] = liste[position - 1]
            position -= 1

        liste[position] = valeur_actuelle

ma_liste = [12, 5, 8, 3, 20, 15, 6]
tri_insertion(ma_liste)
print("Liste triée par insertion :", ma_liste)
