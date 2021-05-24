import char_to_bit

def rotr(n, x):
    mask = 2**32 - 1
    right = (x >> n) & mask
    left  = (x << 32-n) & mask
    result = right | left
    return result & (2 ** 32 - 1) 
