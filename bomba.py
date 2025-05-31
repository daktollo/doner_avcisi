from ayarlar import *
import pygame
from utils import hucre_sec, hucre_dolu_mu

class Bomba:
    def __init__(self):
        self.bomba = pygame.image.load("resimler/bomb.png")
        self.bomba = pygame.transform.scale(self.bomba, (HUCRE_GENISLIGI, HUCRE_GENISLIGI))

        self.x = hucre_sec()
        self.y = hucre_sec()

class BombaYonetici:
    def __init__(self):
        self.bombalar = []

    def bombalari_olustur(self, robot, kebab):
        nesneler = self.bombalar + [robot, kebab]
        sayac = 0
        while sayac < BOMBA_SAYISI:
            bomba = Bomba()
            if not hucre_dolu_mu(bomba, nesneler):
                self.bombalar.append(bomba)
                sayac += 1

    def bombalari_ciz(self, ekran):
        for bomba_nesnesi in self.bombalar:
            ekran.blit(bomba_nesnesi.bomba, (bomba_nesnesi.x, bomba_nesnesi.y))


if __name__ == "__main__":
    bomba_yonetici = BombaYonetici()
    bomba_yonetici.bombalari_olustur()
    print(bomba_yonetici.bombalar[0].x)




