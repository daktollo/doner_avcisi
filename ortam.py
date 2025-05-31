import pygame
from ayarlar import *
from bomba import BombaYonetici
from robot import Robot
from kebab import Kebab

def yerlestir():
    robot = Robot()
    kebab = Kebab()
    while True:
        if (robot.x, robot.y) == (kebab.x, kebab.y):
            kebab = Kebab()
        else:
            break
    
    bomba_yonetici = BombaYonetici()
    bomba_yonetici.bombalari_olustur(robot, kebab)

    return robot, kebab, bomba_yonetici


class OyunAlani:

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.ekran = pygame.display.set_mode((EKRAN_GENISLIGI, EKRAN_YUKSEKLIGI))


    def reset(self):
        self.robot, self.kebab, self.bomba_yonetici  = yerlestir()

    def get_obs(self):
        obs = [0,0,0,0,0,0,0,0]

        for bomba in self.bomba_yonetici.bombalar:
            if self.robot.x + HUCRE_GENISLIGI == bomba.x and self.robot.y == bomba.y:
                obs[2] = 1
            if self.robot.x - HUCRE_GENISLIGI == bomba.x and self.robot.y == bomba.y:
                obs[3] = 1
            if self.robot.x == bomba.x and self.robot.y + HUCRE_GENISLIGI == bomba.y:
                obs[1] = 1
            if self.robot.x == bomba.x and self.robot.y - HUCRE_GENISLIGI == bomba.y:
                obs[0] = 1

        return obs

    
    def render(self):
        self.ekran.fill((255, 255, 255))
        for i in range(0, EKRAN_GENISLIGI, HUCRE_GENISLIGI):
            pygame.draw.line(self.ekran, (0, 0, 0), (i, 0), (i, EKRAN_YUKSEKLIGI))

        for i in range(0, EKRAN_YUKSEKLIGI, HUCRE_GENISLIGI):
            pygame.draw.line(self.ekran, (0, 0, 0), (0, i), (EKRAN_GENISLIGI, i))

        self.robot.ciz(self.ekran)
        self.kebab.ciz(self.ekran)
        self.bomba_yonetici.bombalari_ciz(self.ekran)

        pygame.display.flip()
        self.clock.tick(OYUN_HIZI)
