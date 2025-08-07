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
max_adim = 30

if ui:
    pygame.init()

env = OyunAlani(ui)
q_ajani = QAjani()
toplam_oduller = []

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
        yeni_durum, alinan_odul, oyun_bitti = env.adim(aksiyon)
        toplam_odul += alinan_odul

        q_ajani.guncelle_q_degeri(obs, aksiyon, alinan_odul, yeni_durum)
        if oyun_bitti:
            if ui:
                env.render()
            break
        obs = yeni_durum

    writer.add_scalar("odul", toplam_odul, i)
    toplam_oduller.append(toplam_odul)
    writer.add_scalar("eps_sonu_ortalama_odul", sum(toplam_oduller[:])/len(toplam_oduller), i)
    writer.add_scalar("epsilon", q_ajani.epsilon, i)  # Epsilon değerini de logla
    
    # Epsilon değerini güncelle
    q_ajani.epsilon_guncelle()

    if i % 100 == 0:
        avg_odul = sum(toplam_oduller[-100:]) / 100
        writer.add_scalar("ortalama_odul", avg_odul, i)  # Son 100 oyunun ortalama ödülünü logla
        q_ajani.kayit()