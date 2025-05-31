from ayarlar import *
import random

def hucre_sec():
    hucre = random.randint(0, HUCRE_SAYISI - 1)
    return hucre*HUCRE_GENISLIGI


def hucre_dolu_mu(yeni_nesne, nesneler):
    for nesne in nesneler:
        if nesne.x == yeni_nesne.x and nesne.y == yeni_nesne.y:
            return True
    
    return False


