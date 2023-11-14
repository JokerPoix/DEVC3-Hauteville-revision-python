phrase = input("Entrez une phrase : ")

majuscules = phrase.upper()
print("En majuscules :", majuscules)

minuscules = phrase.lower()
print("En minuscules :", minuscules)

mots = len(phrase.split())
print("Nombre de mots :", mots)