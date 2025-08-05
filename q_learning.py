import pickle

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

    def guncelle_q_degeri(self, durum, aksiyon, alinan_odul, yeni_durum=None):
        """        Q-değerini günceller.
        """
        durum = tuple(durum) # [0, 0, 0, 0, 0, 0, 0, 0] -> (0, 0, 0, 0, 0, 0, 0, 0) d
        aksiyon = tuple(aksiyon) # [0, 0, 0, 0] -> (0, 0, 0, 0) a

        mevcut_q = self.q_table.get((durum, aksiyon), 0)
        max_q_yeni = max(self.q_table.get((yeni_durum, one_hot_encode(a)), 0) for a in range(4))
        yeni_q = mevcut_q + self.alfa * (alinan_odul + self.discount_factor * max_q_yeni - mevcut_q)
        self.q_table[(durum, aksiyon)] = yeni_q


    def aksiyon_sec(self, durum):
        """
        Duruma göre en iyi aksiyonu seçer.
        """
        max_aksiyon = None
        max_odul = None
        for i in range(4):
            aksiyon = [0, 0, 0, 0]
            aksiyon[i] = 1  # i. ak siyonu seç
            odul = self.q_degerini_al(durum, aksiyon)  # yukari
            if max_aksiyon is None:
                max_aksiyon = aksiyon
                max_odul = odul

            elif odul > max_odul:
                max_aksiyon = aksiyon
                max_odul = odul

        return max_aksiyon
    
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