ip = input("Entrez une adresse IP : ")
morceaux = ip.split(".")

valide = True

if len(morceaux) != 3:
    valide = False

if morceaux[0] > "255" or morceaux[1] > "255" or morceaux[2] > "255":
    valide = False

if valide:
    print("IP valide")
else:
    print("IP invalide")
