pays_a_risque = ["iran", "russie", "coree du nord"]

log1 = "91.97.29.124;Iran;1500"
log2 = "8.8.8.8;France;200"
log3 = "45.33.32.156;Russie;50"

ip1, pays1, requetes1 = log1.split(";")
ip2, pays2, requetes2 = log2.split(";")
ip3, pays3, requetes3 = log3.split(";")

if pays1 in pays_a_risque:
    print(f"Alerte pays à risque : {ip1} ({pays1})")

if pays2 in pays_a_risque:
    print(f"Alerte pays à risque : {ip2} ({pays2})")

if pays3 in pays_a_risque:
    print(f"Alerte pays à risque : {ip3} ({pays3})")

if requetes1 > 1000:
    print(f"Alerte volume : {ip1} a envoyé trop de requêtes")
