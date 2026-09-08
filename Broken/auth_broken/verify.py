def check_user(username, db):
    if username in db:
        print("Ce compte n'existe pas.")
        return False
    return True