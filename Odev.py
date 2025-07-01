sehir = ["Berlin", "Dortmund", "Strazbourg", "Leipzig", "Ankara", "İstanbul", "London"]

silinen_deger = sehir.pop()
print(f"Sondan silinen değer: {silinen_deger}")

index_ile_silinen = sehir.pop(3)
print(f"İndex 3'teki silinen değer: {index_ile_silinen}")

print(f"Güncel liste: {sehir}")

try:    
    sil = input("Silmek için bir şehir ismi girin: ")
    sehir.remove(sil)
    print(f"Silinen değer: {sil}")
    print(f"Güncel liste: {sehir}")
except ValueError:
    print(f"Hata: '{sil}' listede bulunamadı.")