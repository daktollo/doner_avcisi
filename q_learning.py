import pickle
import numpy as np

def one_hot_encode(action):
    """
    Aksiyonları one-hot encoding formatına dönüştürür.
    """
    encoded = [0] * 4  # 4 aksiyon için
    encoded[action] = 1
    return encoded

class QAjani:
    def __init__(self,alfa=0.1, discount_factor=0.9): 
        self.q_table = {}
        self.alfa = alfa
        self.discount_factor = discount_factor

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
        Duruma göre en iyi aksiyonu seçer.
        """
        odul_degerleri = [self.q_table.get((tuple(durum), tuple(one_hot_encode(a))), 0) for a in range(4)]

        if all(value == 0 for value in odul_degerleri):
            # Eğer tüm Q-değerleri 0 ise rastgele aksiyon seç
            return one_hot_encode(np.random.choice(range(4)))
        
        max_aksiyon = np.argmax(odul_degerleri)
        return one_hot_encode(max_aksiyon)
    
    def kayit(self):
        with open("son_tablo.pkl", "wb") as dosya:
            pickle.dump(self.q_table, dosya)

    def okuma():
        with open("son_tablo.pkl", "rb") as dosya:
            q_table = pickle.load(dosya)
        
        return q_table
        















""""
        mevcut_q = self.q_table.get((durum, aksiyon), 0)
        max_q_yeni = max(self.q_table.get((yeni_durum, a), 0) for a in range(4))
        yeni_q = mevcut_q + 0.1 * (alinan_odul + 0.9 * max_q_yeni - mevcut_q)
        self.q_table[(durum, aksiyon)] = yeni_q
"""