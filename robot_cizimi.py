import pygame
from ayarlar import *
from bomba import BombaYonetici
from ortam import OyunAlani

pygame.init()

env = OyunAlani()
env.reset()

oyun_devam = True

while oyun_devam:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            oyun_devam = False
        
        if olay.type == pygame.KEYDOWN:

            if olay.key == pygame.K_UP:
                if not env.robot.y - env.robot.hiz < 0:
                    env.robot.y -= env.robot.hiz

            if olay.key == pygame.K_DOWN:
                if not env.robot.y + env.robot.hiz >= EKRAN_YUKSEKLIGI:
                    env.robot.y += env.robot.hiz

            if olay.key == pygame.K_RIGHT:
                if not env.robot.x + env.robot.hiz >= EKRAN_GENISLIGI:
                    env.robot.x += env.robot.hiz

            if olay.key == pygame.K_LEFT:
                if not env.robot.x - env.robot.hiz < 0:
                    env.robot.x -= env.robot.hiz
                    
    env.render()
    print(env.get_obs())



pygame.quit()