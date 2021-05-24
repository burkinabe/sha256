def charToBit(t_str):
    # Python3 code to demonstrate working of
    # Converting String to binary
    # Using join() + ord() + format()

    # initializing string
    test_str = t_str
    # using join() + ord() + format()
    # Converting String to binary
    res = ''.join(format(ord(i), '08b') for i in test_str)
    return str(res)
