import rotr
import shr

def sigma0(x):
    return rotr.rotr(7, x) ^ rotr.rotr(18, x) ^ shr.shr(3, x)

