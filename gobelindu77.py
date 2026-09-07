logs = [
    {"ip": "10.0.0.5",       "country": "France",   "port": 443,  "requetes": 12,   "chemin": "/intranet/accueil"},
    {"ip": "91.97.29.124",   "country": "Iran",     "port": 22,   "requetes": 8400, "chemin": "/admin/login?user=gobelindu77"},
    {"ip": "185.220.101.42", "country": "Russie",   "port": 3389, "requetes": 1500, "chemin": "/rdp/session?user=administrateur"},
    {"ip": "10.0.0.8",       "country": "France",   "port": 80,   "requetes": 340,  "chemin": "/intranet/rh?user=m.dupont"},
    {"ip": "91.97.29.124",   "country": "Iran",     "port": 3389, "requetes": 120,  "chemin": "/rdp/session?user=gobelindu77"},
    {"ip": "10.0.0.5",       "country": "France",   "port": 22,   "requetes": 6200, "chemin": "/admin/login?user=gobelindu77"},
    {"ip": "45.83.64.1",     "country": "Pays-Bas", "port": 443,  "requetes": 90,   "chemin": "/index.html"},
    {"ip": "192.168.1.20",   "country": "France",   "port": 8080, "requetes": 45,   "chemin": "/api/status"},
    {"ip": "185.220.101.42", "country": "Russie",   "port": 22,   "requetes": 3100, "chemin": "/admin/login?user=root"},
    {"ip": "203.0.113.9",    "country": "Bresil",   "port": 80,                     "chemin": "/wp-login.php?user=admin"},
]

'''
Vous etes analyste CTI. Votre collegue vient de vous transmettre ces logs.

Vous devez ecrire un programme capable de :
  - n'afficher que les connexions provenant de l'exterieur du reseau ;
  - filtrer ces connexions par nom d'utilisateur ;
  - afficher le nombre total de requetes par IP.

Chaque etape doit fonctionner avant de passer a la suivante.
'''


'''
Etape 1 - Ne garder que les connexions externes.

Une IP est interne si elle commence par "10." ou "192.168.".

Indices : entree["ip"] pour lire une valeur du dictionnaire.
          .startswith("10.") pour tester un debut de chaine.
          or pour combiner les deux tests.
          return True / return False.
'''
def is_relevant(entree):
    """Retourne True si la connexion vient de l'exterieur du reseau."""
    ...


'''
Etape 2 - Extraire le nom d'utilisateur du chemin.

Le nom se trouve apres "user=". Attention : certains chemins n'en ont pas.
Que doit renvoyer la fonction dans ce cas ?

Indices : "user=" in chemin pour verifier la presence AVANT de decouper.
          chemin.split("user=") coupe la chaine et renvoie une liste.
          Prenez ensuite le bon element de cette liste : [0] ou [1] ?
          Testez d'abord print(chemin.split("user=")) pour voir le resultat.
'''
def get_user(entree):
    """Retourne le nom d'utilisateur du chemin, ou une chaine vide."""
    ...


'''
Etape 3 - Filtrer par utilisateur.

Testez avec "gobelindu77". Combien d'IP differentes utilisent ce compte ?

Indices : creez une liste vide, parcourez logs avec une boucle for,
          appelez get_user() sur chaque entree, comparez avec ==,
          et utilisez .append() quand ca correspond.
'''
def filter_by_user(logs, utilisateur):
    """Retourne la liste des connexions liees a cet utilisateur."""
    ...


'''
Etape 4 - Compter les requetes par IP.

Une meme IP apparait sur plusieurs lignes : il faut additionner.
Attention : une entree du journal n'a pas de cle "requetes".

Indices : partez d'un dictionnaire vide compteur = {}.
          entree.get("requetes", 0) evite le KeyError sur la cle manquante.
          Le motif du comptage :
              compteur[ip] = compteur.get(ip, 0) + ...
'''
def count_by_ip(logs):
    """Retourne un dictionnaire {ip: total des requetes}."""
    ...


'''
Etape 5 - Afficher le rapport.

Cette fonction affiche, elle ne calcule pas : elle appelle les precedentes.

Indices : une boucle for + if is_relevant(entree) pour la premiere partie.
          .items() pour parcourir le dictionnaire de l'etape 4.
          Les f-strings pour mettre en forme :
              print(f"{ip} : {total} requetes")
'''
def print_report(logs):
    """Affiche les connexions externes et le total de requetes par IP."""
    ...