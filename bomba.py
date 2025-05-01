from ayarlar import *
import pygame
from utils import hucre_sec

class Bomba:
    def __init__(self):
        self.bomba = pygame.image.load("resimler/bomb.png")
        self.bomba = pygame.transform.scale(self.bomba, (HUCRE_GENISLIGI, HUCRE_GENISLIGI))

        self.x = hucre_sec()
        self.y = hucre_sec()

class BombaYonetici:
    def __init__(self, ekran):
        self.bombalar = []
        self.ekran = ekran
        self.bombalari_olustur()

    def bombalari_olustur(self):
        for i in range(BOMBA_SAYISI):
            bomba = Bomba()
            self.bombalar.append(bomba)

    def bombalari_ciz(self):
        for bomba_nesnesi in self.bombalar:
            self.ekran.blit(bomba_nesnesi.bomba, (bomba_nesnesi.x, bomba_nesnesi.y))

if __name__ == "__main__":
    bomba_yonetici = BombaYonetici()
    bomba_yonetici.bombalari_olustur()
    print(bomba_yonetici.bombalar[0].x)




