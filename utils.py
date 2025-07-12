from ayarlar import *
import random
from collections import deque

def hucre_sec():
    hucre = random.randint(0, HUCRE_SAYISI - 1)
    return hucre*HUCRE_GENISLIGI


def hucre_dolu_mu(yeni_nesne, nesneler):
    for nesne in nesneler:
        if nesne.x == yeni_nesne.x and nesne.y == yeni_nesne.y:
            return True
    
    return False


def yol_bulunabilir_mi(robot_pos, kebab_pos, bomba_pozisyonlari):
    """
    BFS algoritması ile robotun kebaba ulaşabilir olup olmadığını kontrol eder
    """
    # Grid boyutları
    grid_x = EKRAN_GENISLIGI // HUCRE_GENISLIGI
    grid_y = EKRAN_YUKSEKLIGI // HUCRE_GENISLIGI
    
    # Bomba pozisyonlarını grid koordinatlarına çevir
    bomba_grid = set()
    for bomba_x, bomba_y in bomba_pozisyonlari:
        grid_bomba_x = bomba_x // HUCRE_GENISLIGI
        grid_bomba_y = bomba_y // HUCRE_GENISLIGI
        bomba_grid.add((grid_bomba_x, grid_bomba_y))
    
    # Başlangıç ve hedef pozisyonları grid koordinatlarına çevir
    start_x = robot_pos[0] // HUCRE_GENISLIGI
    start_y = robot_pos[1] // HUCRE_GENISLIGI
    end_x = kebab_pos[0] // HUCRE_GENISLIGI
    end_y = kebab_pos[1] // HUCRE_GENISLIGI
    
    # BFS için kuyruk ve ziyaret edilen hücreler
    kuyruk = deque([(start_x, start_y)])
    ziyaret_edilen = set()
    ziyaret_edilen.add((start_x, start_y))
    
    # 4 yön: yukarı, aşağı, sağ, sol
    yonler = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    
    while kuyruk:
        x, y = kuyruk.popleft()
        
        # Hedefe ulaştık mı?
        if x == end_x and y == end_y:
            return True
        
        # Komşu hücreleri kontrol et
        for dx, dy in yonler:
            yeni_x, yeni_y = x + dx, y + dy
            
            # Sınırlar içinde mi?
            if 0 <= yeni_x < grid_x and 0 <= yeni_y < grid_y:
                # Daha önce ziyaret edilmemiş ve bomba yok mu?
                if (yeni_x, yeni_y) not in ziyaret_edilen and (yeni_x, yeni_y) not in bomba_grid:
                    ziyaret_edilen.add((yeni_x, yeni_y))
                    kuyruk.append((yeni_x, yeni_y))
    
    return False


