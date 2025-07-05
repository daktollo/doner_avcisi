import pickle

liste = []

with open("sadsad.pkl", "wb") as dosya:
    pickle.dump(liste, dosya)


with open("sadsad.pkl", "rb") as dosya:
    pickle.load(dosya)







