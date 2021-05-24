def charToBit(t_str):
    test_str = t_str
    res = ''.join(format(ord(i), '08b') for i in test_str)
    return str(res)
