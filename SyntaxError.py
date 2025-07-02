try:
    sayi1 = int(input("Birinci sayı:")) 
    sayi2 = int(input("İkinci Sayı:"))
    sonuc = sayi1 + sayi2
    print(f"Toplama sonucu: {sonuc}")
except SyntaxError:
    print(f"Kodlama yazım hatası.")