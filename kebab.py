import pygame
from ayarlar import *
from utils import hucre_sec


class Kebab:
    def __init__(self):
        self.resim = pygame.image.load("resimler/kebab.png")
        self.resim = pygame.transform.scale(self.resim, (HUCRE_GENISLIGI, HUCRE_GENISLIGI))

        self.x = hucre_sec()
        self.y = hucre_sec()
        
    def ciz(self, ekran):
        ekran.blit(self.resim, (self.x, self.y))