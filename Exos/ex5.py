def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)

nombre = int(input("Entrez un nombre pour calculer sa factorielle : "))

if nombre < 0:
    print("La factorielle n'est définie que pour les entiers positifs.")
else:
    resultat = factorielle(nombre)
    print(f"La factorielle de {nombre} est : {resultat}")