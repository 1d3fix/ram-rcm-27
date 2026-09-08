mot_de_passe = input("Choisissez un mot de passe : ")

longueur_ok = len(mot_de_passe) >= 8
contient_chiffre = mot_de_passe.isdigit()

if longueur_ok and contient_chiffre:
    print(f"Mot de passe accepté : {mot_de_passe}")
else:
    print("Mot de passe trop faible")
