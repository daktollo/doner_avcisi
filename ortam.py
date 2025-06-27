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

    def _tehlike_konumu(self, obs):
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
    
    def _odul_konumu(self, obs):
        if self.robot.y > self.kebab.y:
            obs[4] = 1
        if self.robot.y < self.kebab.y:
            obs[5] = 1
        if self.robot.x < self.kebab.x:
            obs[6] = 1
        if self.robot.x > self.kebab.x:
            obs[7] = 1

        return obs


    def get_obs(self):
        obs = [0,0,0,0,0,0,0,0] # yukari, asagi, sag, sol, yukari, asagi, sag, sol

        obs = self._tehlike_konumu(obs)
        obs = self._odul_konumu(obs)

        return obs
    
    def _bombaya_carpma(self):
        for bomba in self.bomba_yonetici.bombalar:
            if self.robot.x == bomba.x and self.robot.y == bomba.y:
                return True
           
        return False
    
    def _odul_carpma(self):
        if self.robot.x == self.kebab.x and self.robot.y == self.kebab.y:
            return True
        return False


    
    def get_odul(self):
        odul = 0
        if self._bombaya_carpma():
            odul += BOMBA_CEZA
        if self._odul_carpma():
            odul += KEBAB_ODUL
        
        return odul
    
    def _robot_hareket_ettir(self, aksiyon):
        if aksiyon[0] == 1: # yukari
            if not self.robot.y - self.robot.hiz < 0:
                self.robot.y -= self.robot.hiz

        elif aksiyon[1] == 1:  # asagi
            if not self.robot.y + self.robot.hiz >= EKRAN_YUKSEKLIGI:
                self.robot.y += self.robot.hiz

        elif aksiyon[2] == 1: # sag
            if not self.robot.x + self.robot.hiz >= EKRAN_GENISLIGI:
                self.robot.x += self.robot.hiz

        elif aksiyon[3] == 1: # sol
            if not self.robot.x - self.robot.hiz < 0:
                self.robot.x -= self.robot.hiz

    
    def adim(self, aksiyon):
        self._robot_hareket_ettir(aksiyon)

        alinan_odul = self.get_odul()
        oyun_bitti = self._bombaya_carpma() or self._odul_carpma()
        yeni_durum = self.get_obs()

        return yeni_durum, alinan_odul, oyun_bitti


    
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
