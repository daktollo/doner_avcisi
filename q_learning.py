class QAjani:
    def __init__(self, alpha=0.1, gamma=0.9):
        """
        Q-Learning ajanı
        
        Args:
            alpha (float): Öğrenme oranı (learning rate) - 0.1 varsayılan
            gamma (float): İndirim faktörü (discount factor) - 0.9 varsayılan
        """
        self.q_table = {}
        self.alpha = alpha  # Öğrenme oranı
        self.gamma = gamma  # İndirim faktörü

    def q_degerini_al(self, durum, aksiyon):
        """
        Q-değerini alır.
        Eğer Q-değeri yoksa, 0 döner.
        """
        durum = tuple(durum)
        aksiyon = tuple(aksiyon)
        return self.q_table.get((durum, aksiyon), 0)

    def guncelle_q_degeri(self, durum, aksiyon, alinan_odul, yeni_durum=None):
        """
        Q-değerini gerçek Q-learning algoritmasına göre günceller.
        
        Q-Learning Formülü:
        Q(s,a) = Q(s,a) + α[r + γ * max(Q(s',a')) - Q(s,a)]
        
        Adım adım açıklama:
        1. Mevcut Q-değerini al: Q(s,a)
        2. Yeni durumda en iyi aksiyonun Q-değerini bul: max(Q(s',a'))
        3. Temporal Difference (TD) hatasını hesapla: r + γ * max(Q(s',a')) - Q(s,a)
        4. Q-değerini güncelle: Q(s,a) = Q(s,a) + α * TD_hatası
        
        Args:
            durum: Mevcut durum (state)
            aksiyon: Seçilen aksiyon (action)
            alinan_odul: Alınan ödül (reward)
            yeni_durum: Yeni durum (next state) - None ise terminal durum
        """
        # Adım 1: Tuple formatına çevir
        durum = tuple(durum)
        aksiyon = tuple(aksiyon)
        
        # Adım 2: Mevcut Q-değerini al
        mevcut_q = self.q_degerini_al(durum, aksiyon)
        
        # Adım 3: Yeni durumda en iyi Q-değerini bul
        if yeni_durum is None:
            # Terminal durum - gelecek ödül yok
            max_q_yeni = 0
        else:
            yeni_durum = tuple(yeni_durum)
            # Yeni durumda tüm aksiyonları dene ve en yüksek Q-değerini bul
            max_q_yeni = 0
            for i in range(4):
                test_aksiyon = [0, 0, 0, 0]
                test_aksiyon[i] = 1
                test_aksiyon = tuple(test_aksiyon)
                q_degeri = self.q_degerini_al(yeni_durum, test_aksiyon)
                max_q_yeni = max(max_q_yeni, q_degeri)
        
        # Adım 4: Temporal Difference (TD) hatasını hesapla
        td_hatasi = alinan_odul + self.gamma * max_q_yeni - mevcut_q
        
        # Adım 5: Q-değerini güncelle
        yeni_q = mevcut_q + self.alpha * td_hatasi
        
        # Adım 6: Güncellenmiş Q-değerini kaydet
        self.q_table[(durum, aksiyon)] = yeni_q
        
        # Debug için bilgi yazdır (isteğe bağlı)
        # print(f"Q-güncelleme: Q({durum},{aksiyon}) = {mevcut_q:.3f} -> {yeni_q:.3f}")
        # print(f"TD hatası: {td_hatasi:.3f}, Ödül: {alinan_odul}, Max Q(s'): {max_q_yeni:.3f}")


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