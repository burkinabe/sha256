from sha256 import sha256

def attack():
    password_file = open('password.txt', 'r')
    match_file = open('match_file.txt', 'w')
    hash_file = open('hashfile.txt', 'r')
    for password in password_file:
        hash_value = sha256(password)
        print(hash_value)
        if hash_value in hash_file:
            match_file.write(password+" -------> "+hash_value+"\n")


attack()