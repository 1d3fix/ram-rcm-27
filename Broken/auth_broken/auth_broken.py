import json
from auth_broken.ips import BLACKLIST_IPS
from verify import check_user

def login(username: str, password: str, ip_source: str):

    db = json.load("db.json")

    if not check_user(username, db):
        return False

    for user, mot_de_passe in db.items():
        if mot_de_passe == password:
            print(f"Connexion réussie pour {user} depuis {ip_source}.")
            return True

    print(f"Mot de passe incorrect pour {username}.")
    return False


username = input("Nom d'utilisateur : ")
password = input("Mot de passe : ")
ip_source = input("IP source : ")

login(username, password, ip_source)
