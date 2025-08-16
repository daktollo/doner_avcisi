import pickle
import numpy as np
import random

def one_hot_encode(action):
    """
    Aksiyonları one-hot encoding formatına dönüştürür.
    """
    encoded = [0] * 4  # 4 aksiyon için
    encoded[action] = 1
    return encoded

class QAjani:
    def __init__(self,alfa=0.2, discount_factor=0.85, epsilon=1.0, epsilon_min=0.05, epsilon_decay=0.995): 
        self.q_table = {}
        self.alfa = alfa
        self.discount_factor = discount_factor
        self.epsilon = epsilon  # Keşif oranı
        self.epsilon_min = epsilon_min  # Minimum epsilon değeri
        self.epsilon_decay = epsilon_decay  # Epsilon azalma oranı

    def q_degerini_al(self, durum, aksiyon):
        """
        Q-değerini alır.
        Eğer Q-değeri yoksa, 0 döner.
        """
        durum = tuple(durum)
        aksiyon = tuple(aksiyon)
        return self.q_table.get((durum, aksiyon), 0)

    def guncelle_q_degeri(self, durum, aksiyon, alinan_odul, yeni_durum):
        """        Q-değerini günceller.
        """
        durum = tuple(durum) # [0, 0, 0, 0, 0, 0, 0, 0] -> (0, 0, 0, 0, 0, 0, 0, 0) d
        aksiyon = tuple(aksiyon) # [0, 0, 0, 0] -> (0, 0, 0, 0) a

        mevcut_q = self.q_table.get((durum, aksiyon), 0)

        yeni_durum = tuple(yeni_durum)  # yeni_durum'u da tuple'a çevir
        max_q_yeni = max(self.q_table.get((yeni_durum, tuple(one_hot_encode(a))), 0) for a in range(4))
        
        yeni_q = mevcut_q + self.alfa * (alinan_odul + self.discount_factor * max_q_yeni - mevcut_q)
        self.q_table[(durum, aksiyon)] = yeni_q


    def aksiyon_sec(self, durum):
        """
        Duruma göre epsilon-greedy stratejisi ile aksiyon seçer.
        """
        # Epsilon-greedy: rastgele sayı epsilon'dan küçükse keşif yap
        if random.uniform(0, 1) < self.epsilon:
            # Keşif: rastgele aksiyon seç
            return one_hot_encode(np.random.choice(range(4)))
        else:
            # Sömürü: en iyi aksiyonu seç
            odul_degerleri = [self.q_table.get((tuple(durum), tuple(one_hot_encode(a))), 0) for a in range(4)]
            if all(deger == 0 for deger in odul_degerleri):
                # Eğer tüm Q-değerleri sıfırsa rastgele aksiyon seç
                return one_hot_encode(np.random.choice(range(4)))
            max_aksiyon = np.argmax(odul_degerleri)
            return one_hot_encode(max_aksiyon)
    
    def epsilon_guncelle(self):
        """
        Epsilon değerini günceller (azaltır).
        """
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
        
    def kayit(self):
        with open("son_tablo.pkl", "wb") as dosya:
            pickle.dump(self.q_table, dosya)

    def okuma(self):
        with open("son_tablo.pkl", "rb") as dosya:
            q_table = pickle.load(dosya)
        self.q_table = q_table
        return q_table
        















""""
        mevcut_q = self.q_table.get((durum, aksiyon), 0)
        max_q_yeni = max(self.q_table.get((yeni_durum, a), 0) for a in range(4))
        yeni_q = mevcut_q + 0.1 * (alinan_odul + 0.9 * max_q_yeni - mevcut_q)
        self.q_table[(durum, aksiyon)] = yeni_q
"""