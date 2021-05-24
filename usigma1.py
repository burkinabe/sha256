from rotr import rotr
from shr import shr

def usigma1(x):
  return rotr(6, x) ^ rotr(11, x) ^ rotr(25, x)