import pygame
from ayarlar import *
from bomba import BombaYonetici
from ortam import OyunAlani
from q_learning import QAjani
import time
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter()

ui = True
eps = 10000
max_adim = 25

if ui:
    pygame.init()

env = OyunAlani(ui)
q_ajani = QAjani()
for i in range(eps):
    obs = env.reset()
    toplam_odul = 0
    for j in range(max_adim):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                q_ajani.kayit()
                pygame.quit()
                exit()
        if ui:
            env.render()

        aksiyon = q_ajani.aksiyon_sec(obs)
        print(f"Aksiyon: {aksiyon}")
        yeni_durum, alinan_odul, oyun_bitti = env.adim(aksiyon)
        toplam_odul += alinan_odul

        q_ajani.guncelle_q_degeri(obs, aksiyon, alinan_odul, yeni_durum)
        if oyun_bitti:
            break
        obs = yeni_durum

    writer.add_scalar("odul", toplam_odul, i)

    if i % 30 == 0:
        q_ajani.kayit()