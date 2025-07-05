import pygame
from ayarlar import *
from bomba import BombaYonetici
from ortam import OyunAlani
from q_learning import QAjani
import time
import pickle
import os

# Koşum ayarları
ui = True  # UI'yi aktif et
max_adim = 50  # Maksimum adım sayısı
q_table_dosya = "/home/daktollo/SEP/Meliora/RL/doner_avcisi/q_tables/q_table_epoch_4000.pkl"  # Yüklenecek Q-tablosu dosyası

# Pygame'i başlat
pygame.init()

# Ortam ve ajanı oluştur
env = OyunAlani(ui)
q_ajani = QAjani()

# Koşum modunda epsilon = 0 (rastgele seçim yok, sadece en iyi aksiyonu seç)
q_ajani.epsilon_ayarla(0)

# Eğitilmiş Q-tablosunu yükle
if os.path.exists(q_table_dosya):
    q_ajani.q_table_yukle(q_table_dosya)
    print(f"Q-tablosu başarıyla yüklendi. Epsilon değeri: {q_ajani.epsilon}")
else:
    print(f"Q-tablosu dosyası bulunamadı: {q_table_dosya}")
    print("Mevcut Q-tablosu dosyalarını kontrol edin:")
    if os.path.exists("q_tables"):
        for dosya in os.listdir("q_tables"):
            print(f"  - {dosya}")
    exit()

print("Koşum başlıyor... (ESC ile çıkış)")
print("Ajan tamamen eğitilmiş haliyle oynuyor (epsilon = 0)")

# Ana oyun döngüsü
calisir = True
episode = 0

while calisir:
    episode += 1
    print(f"\n--- Episode {episode} ---")
    
    obs = env.reset()
    toplam_reward = 0
    adim_sayisi = 0
    
    for j in range(max_adim):
        # Pygame olaylarını kontrol et
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                calisir = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    calisir = False
                    break
        
        if not calisir:
            break
        
        # Ortamı render et
        env.render()
        
        # Ajan aksiyonu seç (epsilon = 0 olduğu için sadece en iyi aksiyon)
        aksiyon = q_ajani.aksiyon_sec(obs)
        
        # Aksiyonu uygula
        yeni_durum, alinan_odul, oyun_bitti = env.adim(aksiyon)
        
        toplam_reward += alinan_odul
        adim_sayisi += 1
        

        if oyun_bitti:
            print(f"Oyun bitti! Toplam ödül: {toplam_reward}, Adım sayısı: {adim_sayisi}")
            break
        
        obs = yeni_durum
        
        # Biraz bekle (görmek için)
        time.sleep(0.1)
    
    if not calisir:
        break
    
    # Episode arası bekleme
    print("Yeni episode için 2 saniye bekleniyor...")
    time.sleep(2)

# Temizlik
pygame.quit()
print("Koşum tamamlandı.")
