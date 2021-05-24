from sigma1 import sigma1
from add import add
from sigma0 import sigma0
from usigma0 import usigma0
from usigma1 import usigma1
from maj import maj
from ch import ch

K = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311]
for k in K:
    k ** (1 / 3.0)
    k * 2 ** 32



# -----------
# Compression - Run compression function on the message schedule and constants
# -----------
# Initial Hash Values = Square roots of the first 8 prime numbers (first 32 bits of the fractional part)
IV = [2, 3, 5, 7, 11, 13, 17, 19]
for iv in IV:
    iv ** (1 / 2.0)
    iv * 2 ** 32


def compression(initial, schedule, constants):
  # state register - set initial values ready for the compression function
  h = initial[7]
  g = initial[6]
  f = initial[5]
  e = initial[4]
  d = initial[3]
  c = initial[2]
  b = initial[1]
  a = initial[0]

  # compression function - update state for every word in the message schedule
  for i in range(63):
    # calculate temporary words
    t1 = add(schedule[i], constants[i], usigma1(e), ch(e, f, g), h)
    t2 = add(usigma0(a), maj(a, b, c))

    # rotate state registers one position and add in temporary words
    h = g
    g = f
    f = e
    e = add(d, t1)
    d = c
    c = b
    b = a
    a = add(t1, t2)

  # Final hash values are previous intermediate hash values added to output of compression function
  hash = [0 for x in range( 8 )]
  hash[7] = add(initial[7], h)
  hash[6] = add(initial[6], g)
  hash[5] = add(initial[5], f)
  hash[4] = add(initial[4], e)
  hash[3] = add(initial[3], d)
  hash[2] = add(initial[2], c)
  hash[1] = add(initial[1], b)
  hash[0] = add(initial[0], a)
  #hash = initial.zip(updated).map {|i, u| add(i, u)} # succinct method for adding one array on top of another (but not as readable)

  # return final state
  return hash


schedule = [2148534274, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 2148534274, 835584, 86053896, 4160750391, 2827242097, 29557504, 2891759710, 1643149339, 4162606229, 943174880, 2565228367, 3580256609, 3979020798, 2835761637, 2213796368, 4244829688, 2125720534, 320572108, 3545485374, 2118403644, 2763186595, 3393292711, 4213667932, 4166040631, 2292294274, 1932361353, 1035747438, 2896374806, 2880305676, 1607346521, 299247160, 2970850575, 1119300673, 2628099835, 1516912884, 2452596164, 2712176795, 2065407948, 1638475032, 1940861374, 513819148, 409164749, 3975451576, 2273753850, 896139042, 1192406540, 838932523]
print(compression(IV, schedule, K))