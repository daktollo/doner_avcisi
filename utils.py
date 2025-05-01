from ayarlar import *
import random

def hucre_sec():
    hucre = random.randint(0, HUCRE_SAYISI - 1)
    return hucre*HUCRE_GENISLIGI
