try:
    sayi1 = int(input("Birinci sayı:"))
    sayi2 = int(input("İkinci Sayı:"))
    sonuc = sayi1 / sayi2
    print(f"Bölme sonucu: {sonuc}")   
except ZeroDivisionError:
    print(f"Bölme hatası.")