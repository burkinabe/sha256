from sha256 import sha256

def main():
    msg = input()
    print(sha256(msg))


if __name__ == "__main__":
    main()