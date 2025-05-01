import pygame
from ayarlar import *
from utils import hucre_sec
from bomba import BombaYonetici

pygame.init()
clock = pygame.time.Clock()

ekran = pygame.display.set_mode((EKRAN_GENISLIGI, EKRAN_YUKSEKLIGI))

robot_resimi = pygame.image.load("resimler/robot.png")
robot_resimi = pygame.transform.scale(robot_resimi, (HUCRE_GENISLIGI, HUCRE_GENISLIGI))
robot_x = hucre_sec()
robot_y = hucre_sec()
robot_hiz = HUCRE_GENISLIGI

kebab_resimi = pygame.image.load("resimler/kebab.png")
kebab_resimi = pygame.transform.scale(kebab_resimi, (HUCRE_GENISLIGI, HUCRE_GENISLIGI))
kebab_x = hucre_sec()
kebab_y = hucre_sec()

bomba_yonetici = BombaYonetici(ekran)

oyun_devam = True

while oyun_devam:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            oyun_devam = False
        
        if olay.type == pygame.KEYDOWN:

            if olay.key == pygame.K_UP:
                if not robot_y - robot_hiz < 0:
                    robot_y -= robot_hiz

            if olay.key == pygame.K_DOWN:
                if not robot_y + robot_hiz >= EKRAN_YUKSEKLIGI:
                    robot_y += robot_hiz

            if olay.key == pygame.K_RIGHT:
                if not robot_x + robot_hiz >= EKRAN_GENISLIGI:
                    robot_x += robot_hiz

            if olay.key == pygame.K_LEFT:
                if not robot_x - robot_hiz < 0:
                    robot_x -= robot_hiz

    ekran.fill((255, 255, 255))
    for i in range(0, EKRAN_GENISLIGI, HUCRE_GENISLIGI):
        pygame.draw.line(ekran, (0, 0, 0), (i, 0), (i, EKRAN_YUKSEKLIGI))

    for i in range(0, EKRAN_YUKSEKLIGI, HUCRE_GENISLIGI):
        pygame.draw.line(ekran, (0, 0, 0), (0, i), (EKRAN_GENISLIGI, i))


    ekran.blit(robot_resimi, (robot_x, robot_y))
    ekran.blit(kebab_resimi, (kebab_x, kebab_y))
    bomba_yonetici.bombalari_ciz()

    
    
    pygame.display.flip()
    clock.tick(OYUN_HIZI)

pygame.quit()