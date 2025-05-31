import ayarlar
from utils import *
import pygame

class Robot:
    def __init__(self):
        self.x = hucre_sec()
        self.y = hucre_sec()
        self.hiz = HUCRE_GENISLIGI

        self.resim = pygame.image.load("resimler/robot.png")
        self.resim = pygame.transform.scale(self.resim, (HUCRE_GENISLIGI, HUCRE_GENISLIGI))

    def ciz(self, ekran):
        ekran.blit(self.resim, (self.x, self.y))