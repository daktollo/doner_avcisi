import pickle
import os

class QAjani:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        """
        Q-Learning ajanı
        
        Args:
            alpha (float): Öğrenme oranı (learning rate) - 0.1 varsayılan
            gamma (float): İndirim faktörü (discount factor) - 0.9 varsayılan
            epsilon (float): Keşif oranı (exploration rate) - 0.1 varsayılan
        """
        self.q_table = {}
        self.alpha = alpha  # Öğrenme oranı
        self.gamma = gamma  # İndirim faktörü
        self.epsilon = epsilon  # Keşif oranı

    def q_table_yukle(self, dosya_yolu):
        """
        Kaydedilmiş Q-tablosunu yükler.
        
        Args:
            dosya_yolu (str): Q-tablosu dosyasının yolu
        """
        try:
            with open(dosya_yolu, 'rb') as f:
                self.q_table = pickle.load(f)
            print(f"Q-tablosu başarıyla yüklendi: {dosya_yolu}")
            print(f"Yüklenen Q-tablosu boyutu: {len(self.q_table)}")
        except FileNotFoundError:
            print(f"Dosya bulunamadı: {dosya_yolu}")
        except Exception as e:
            print(f"Q-tablosu yüklenirken hata oluştu: {e}")

    def q_table_kaydet(self, dosya_yolu):
        """
        Q-tablosunu kaydeder.
        
        Args:
            dosya_yolu (str): Q-tablosunun kaydedileceği dosya yolu
        """
        try:
            # Klasör yoksa oluştur
            klasor = os.path.dirname(dosya_yolu)
            if klasor and not os.path.exists(klasor):
                os.makedirs(klasor)
            
            with open(dosya_yolu, 'wb') as f:
                pickle.dump(self.q_table, f)
            print(f"Q-tablosu başarıyla kaydedildi: {dosya_yolu}")
        except Exception as e:
            print(f"Q-tablosu kaydedilirken hata oluştu: {e}")

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
        Epsilon-greedy stratejisi ile aksiyon seçer.
        
        - Epsilon olasılıkla rastgele aksiyon seçer (exploration)
        - (1-epsilon) olasılıkla en iyi aksiyonu seçer (exploitation)
        """
        import random
        
        # Epsilon olasılıkla rastgele keşif yap
        if random.random() < self.epsilon:
            # Rastgele aksiyon seç (exploration)
            rastgele_aksiyon_index = random.randint(0, 3)
            aksiyon = [0, 0, 0, 0]
            aksiyon[rastgele_aksiyon_index] = 1
            return aksiyon
        else:
            # En iyi aksiyonu seç (exploitation)
            max_aksiyon = None
            max_odul = None
            for i in range(4):
                aksiyon = [0, 0, 0, 0]
                aksiyon[i] = 1  # i. aksiyonu seç
                odul = self.q_degerini_al(durum, aksiyon)
                if max_aksiyon is None:
                    max_aksiyon = aksiyon
                    max_odul = odul
                elif odul > max_odul:
                    max_aksiyon = aksiyon
                    max_odul = odul
            
            return max_aksiyon
    
    def epsilon_azalt(self, min_epsilon=0.01, azalma_orani=0.995):
        """
        Epsilon değerini zamanla azaltır.
        
        Başlangıçta daha çok keşif, sonra daha çok sömürü yapar.
        
        Args:
            min_epsilon (float): Minimum epsilon değeri
            azalma_orani (float): Epsilon azalma oranı (0.995 = %0.5 azalma)
        """
        if self.epsilon > min_epsilon:
            self.epsilon *= azalma_orani
    
    def epsilon_degerini_al(self):
        """
        Mevcut epsilon değerini döner.
        """
        return self.epsilon
    
    def epsilon_ayarla(self, yeni_epsilon):
        """
        Epsilon değerini belirli bir değere ayarlar.
        
        Args:
            yeni_epsilon (float): Yeni epsilon değeri (0-1 arası)
        """
        if 0 <= yeni_epsilon <= 1:
            self.epsilon = yeni_epsilon
            print(f"Epsilon değeri {yeni_epsilon} olarak ayarlandı")
        else:
            print(f"Hata: Epsilon değeri 0-1 arasında olmalıdır. Verilen: {yeni_epsilon}")