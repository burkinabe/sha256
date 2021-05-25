from sha256 import sha256

def hash():
    f = open('password.txt', 'r')
    hf = open('hashfile.txt', 'w')
    for l in f:
        hf.write(sha256(l)+"\n")


hash()