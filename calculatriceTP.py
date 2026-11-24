print("=== MA CALCULATRICE ===")

continuer = "oui"
historique = []

while continuer == "oui":
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))

    print("1 - Addition")
    print("2 - Soustraction")
    print("3 - Multiplication")
    print("4 - Division")

    choix = input("Choisissez une opération : ")

    if choix == "1":
        resultat = a + b
        print("Résultat :", resultat)
    elif choix == "2":
        resultat = a - b
        print("Résultat :", resultat)
    elif choix == "3":
        resultat = a * b
        print("Résultat :", resultat)
    elif choix == "4":
        if b != 0:
            resultat = a / b
            print("Résultat :", resultat)
        else:
            print("Impossible de diviser par zéro")
            resultat = None
    else:
        print("Choix invalide")
        resultat = None

    if resultat is not None:
        historique.append(f"{a} opération {choix} {b} = {resultat}")

    continuer = input("Voulez-vous faire un autre calcul ? (oui/non) ")

print("\n=== HISTORIQUE DES CALCULS ===")

for calcul in historique:
    print(calcul)

print("Merci d'avoir utilisé la calculatrice !")