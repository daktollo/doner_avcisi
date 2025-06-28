class QAjani:
    def __init__(self):
        self.q_table = {}

    def q_degerini_al(self, durum, aksiyon):
        """
        Q-değerini alır.
        Eğer Q-değeri yoksa, 0 döner.
        """
        pass
    
    def guncelle_q_degeri(self, durum, aksiyon, alinan_odul, yeni_durum=None):
        """        Q-değerini günceller.
        """
        durum = tuple(durum)  # Durumu tuple'a çevir
        aksiyon = tuple(aksiyon)  # Aksiyonu tuple'a çe
        self.q_table[(durum, aksiyon)] = alinan_odul


    def aksiyon_sec(self, durum):
        """
        Duruma göre en iyi aksiyonu seçer.
        """
        return [0,0,0,1]  # Örnek olarak, sadece sol aksiyonu seçiyor [yukari, asagi, sag, sol]
    















""""
        mevcut_q = self.q_table.get((durum, aksiyon), 0)
        max_q_yeni = max(self.q_table.get((yeni_durum, a), 0) for a in range(4))
        yeni_q = mevcut_q + 0.1 * (alinan_odul + 0.9 * max_q_yeni - mevcut_q)
        self.q_table[(durum, aksiyon)] = yeni_q
"""