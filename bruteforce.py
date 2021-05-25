from sha256 import sha256

def attack():
    password_file = open('password.txt', 'r')
    match_file = open('match_file.txt', 'a')
    hash_file = open('hashfile.txt', 'r')
    hash_values = []
    for password in password_file:
        hash_value = sha256(password)
        hash_values.append(hash_value)
        print(hash_value)

    hash_file_content = []
    for line in hash_file:
        hash_file_content.append(line)

    print(hash_file_content)

    for hv in range(len(hash_values)):
        for h_f_c in range(len(hash_file_content)):
            str = hash_file_content[h_f_c].strip("\n")
            if str == hash_values[hv]:
                print(str)
                match_file.write(str+" -------> "+hash_value+"\n")


attack()