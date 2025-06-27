import pygame
from ayarlar import *
from bomba import BombaYonetici
from ortam import OyunAlani

pygame.init()

env = OyunAlani()
env.reset()

oyun_devam = True

while oyun_devam:
    aksiyon = [0,0,0,0] # yukari, asagi, sag, sol

    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            oyun_devam = False
        
        if olay.type == pygame.KEYDOWN:

            if olay.key == pygame.K_UP:
                aksiyon[0] = 1

            if olay.key == pygame.K_DOWN:
                aksiyon[1] = 1

            if olay.key == pygame.K_RIGHT:
                aksiyon[2] = 1

            if olay.key == pygame.K_LEFT:
                aksiyon[3] = 1
                    
    yeni_durum, odul, bitti = env.adim(aksiyon)
    print(yeni_durum, odul, bitti)
    if bitti:
        env.reset()
    env.render()

pygame.quit()