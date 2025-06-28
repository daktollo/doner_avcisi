import pygame
from ayarlar import *
from bomba import BombaYonetici
from ortam import OyunAlani
from q_learning import QAjani
import time

ui = True
eps = 100
max_adim = 20

if ui:
    pygame.init()

env = OyunAlani(ui)
q_ajani = QAjani()
for i in range(eps):
    obs = env.reset()
    for j in range(max_adim):
        if ui:
            env.render()

        aksiyon = q_ajani.aksiyon_sec(obs)
        yeni_durum, alinan_odul, oyun_bitti = env.adim(aksiyon)
        q_ajani.guncelle_q_degeri(obs, aksiyon, alinan_odul)
        if oyun_bitti:
            break
        obs = yeni_durum


print("Eğitim tamamlandı.")
print("Q-Tablosu:")
for key, value in q_ajani.q_table.items():
    print(f"Durum: {key[0]}, Aksiyon: {key[1]}, Q-Değeri: {value}")