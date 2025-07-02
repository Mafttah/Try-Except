liste = [1, 2, 3]
try:
    print(liste[5])
except IndexError:
    print("Hata: Liste sınırları dışında bir index çağırıldı!")