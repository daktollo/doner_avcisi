tablo = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
bombalar = [(2,1)]

tablo = set(tablo) - set(bombalar)
print(tablo)
baslangic = (2,0)
hedef = (2,2)

sira = [baslangic]
bakildi = []

yonler = [(0,-1), (0,1), (1,0), (-1,0)] # yukari, asagi, sag, sol 

while len(sira) > 0:
    bakalicak = sira.pop(0)
