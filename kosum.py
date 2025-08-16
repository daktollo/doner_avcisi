import pygame
from ayarlar import *
from bomba import BombaYonetici
from ortam import OyunAlani
from q_learning import QAjani
import time


pygame.init()

env = OyunAlani(True)
q_ajani = QAjani(epsilon=0)
q_ajani.okuma()


obs = env.reset()
while True:
    env.render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    aksiyon = q_ajani.aksiyon_sec(obs)
    obs, alinan_odul, oyun_bitti = env.adim(aksiyon)
    print("obs:", obs)

    if oyun_bitti:
        env.render()
        time.sleep(2)  # Oyun bittiğinde 2 saniye bekle
        obs = env.reset()

        
