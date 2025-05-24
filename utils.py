from ayarlar import *
import random

def hucre_sec():
    hucre = random.randint(0, HUCRE_SAYISI - 1)
    return hucre*HUCRE_GENISLIGI



def hucre_dolu_mu(yeni_nesne, nesneler):
    yeni_nesne.x

def dolu_mu(self, yeni_bomba):
    for bomba in self.bombalar:
        if bomba.x == yeni_bomba.x and bomba.y == yeni_bomba.y:
            return True
    return False