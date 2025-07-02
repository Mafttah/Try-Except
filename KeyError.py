bilgi = {"ad": "Ali"}
try:
    print(bilgi["soyad"])
except KeyError:
    print("Hata: Anahtar bulunamadı!")