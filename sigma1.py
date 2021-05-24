from rotr import rotr
from shr import shr

def sigma1(x):
  return rotr(17, x) ^ rotr(19, x) ^ shr(10, x)


print(bin(sigma1(0b10000000000000000000000000000000)))