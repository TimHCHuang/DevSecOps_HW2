from werkzeug.security import generate_password_hash, check_password_hash

def set_password(password):
    return generate_password_hash(method='pbkdf2:sha512:150000',
password=password)
def check_password(passwordhash, password):
    return check_password_hash(passwordhash, password)

password = "Testtest"

passwordhash = set_password(password)

if check_password(passwordhash, password) is True:
    print("Check OK \n" + password + "\n" + passwordhash)
