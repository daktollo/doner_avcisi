import pygame
from ayarlar import *
from bomba import BombaYonetici
from ortam import OyunAlani
from q_learning import QAjani
import time
from torch.utils.tensorboard import SummaryWriter

ui = False
eps = 10000
max_adim = 50

if ui:
    pygame.init()

# TensorBoard writer'ı oluştur
writer = SummaryWriter('runs/q_learning')

env = OyunAlani(ui)
q_ajani = QAjani()

# Ortalama reward hesaplamak için liste
reward_listesi = []

for i in range(eps):
    obs = env.reset()
    toplam_reward = 0
    for j in range(max_adim):
        if ui:
            env.render()

        aksiyon = q_ajani.aksiyon_sec(obs)
        yeni_durum, alinan_odul, oyun_bitti = env.adim(aksiyon)
        q_ajani.guncelle_q_degeri(obs, aksiyon, alinan_odul, yeni_durum)
        toplam_reward += alinan_odul
        if oyun_bitti:
            break
        obs = yeni_durum
    
    # Episode sonunda toplam reward'u TensorBoard'a kaydet
    writer.add_scalar('Toplam_Reward', toplam_reward, i)
    
    # Ortalama reward hesaplamak için listeye ekle
    reward_listesi.append(toplam_reward)
    
    # Her 10 episode'da bir ortalama reward hesapla ve kaydet
    if (i + 1) % 10 == 0:
        ortalama_reward = sum(reward_listesi[-10:]) / 10
        writer.add_scalar('Ortalama_Reward', ortalama_reward, i)

# Writer'ı kapat
writer.close()


print("Eğitim tamamlandı.")
print("Q-Tablosu:")
for key, value in q_ajani.q_table.items():
    print(f"Durum: {key[0]}, Aksiyon: {key[1]}, Q-Değeri: {value}")