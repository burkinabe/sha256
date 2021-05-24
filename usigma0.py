from rotr import rotr
from shr import shr

def usigma0(x):
  return rotr(2, x) ^ rotr(13, x) ^ rotr(22, x)


