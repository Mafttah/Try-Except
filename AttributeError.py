try:
    sayi = 5
    sayi.append(10)
except AttributeError as e:
    print(f"Hata yakalandı: {e}")