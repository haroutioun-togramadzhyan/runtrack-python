chaine_base = "abcdefghijklmnopqrstuvwxyz"
repetition = 1

chaine_complete = chaine_base * repetition

taille = len(chaine_complete)
for i in range(taille):
    ligne = chaine_complete[:i].ljust(taille)
    print(ligne)
