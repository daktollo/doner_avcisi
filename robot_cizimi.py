import pygame
from ayarlar import *
from utils import hucre_sec
from bomba import BombaYonetici
from robot import Robot

pygame.init()
clock = pygame.time.Clock()

ekran = pygame.display.set_mode((EKRAN_GENISLIGI, EKRAN_YUKSEKLIGI))

robot = Robot()

kebab_resimi = pygame.image.load("resimler/kebab.png")
kebab_resimi = pygame.transform.scale(kebab_resimi, (HUCRE_GENISLIGI, HUCRE_GENISLIGI))
kebab_x = hucre_sec()
kebab_y = hucre_sec()

bomba_yonetici = BombaYonetici()
oyun_devam = True

while oyun_devam:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            oyun_devam = False
        
        if olay.type == pygame.KEYDOWN:

            if olay.key == pygame.K_UP:
                if not robot.y - robot.hiz < 0:
                    robot.y -= robot.hiz

            if olay.key == pygame.K_DOWN:
                if not robot.y + robot.hiz >= EKRAN_YUKSEKLIGI:
                    robot.y += robot.hiz

            if olay.key == pygame.K_RIGHT:
                if not robot.x + robot.hiz >= EKRAN_GENISLIGI:
                    robot.x += robot.hiz

            if olay.key == pygame.K_LEFT:
                if not robot.x - robot.hiz < 0:
                    robot.x -= robot.hiz

    ekran.fill((255, 255, 255))
    for i in range(0, EKRAN_GENISLIGI, HUCRE_GENISLIGI):
        pygame.draw.line(ekran, (0, 0, 0), (i, 0), (i, EKRAN_YUKSEKLIGI))

    for i in range(0, EKRAN_YUKSEKLIGI, HUCRE_GENISLIGI):
        pygame.draw.line(ekran, (0, 0, 0), (0, i), (EKRAN_GENISLIGI, i))


    ekran.blit(robot.resim, (robot.x, robot.y))
    ekran.blit(kebab_resimi, (kebab_x, kebab_y))
    bomba_yonetici.bombalari_ciz(ekran)

    
    
    pygame.display.flip()
    clock.tick(OYUN_HIZI)

pygame.quit()