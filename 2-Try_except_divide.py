try:
    sayi1 = int(input("Birinci sayı:"))
    sayi2 = int(input("İkinci Sayı:"))
    sonuc = sayi1 / sayi2
    print(f"Bölme sonucu: {sonuc}")
except SyntaxError:
    print(f"Kodlama yazım hatası.")
except TypeError:
    print(f"Type hatası olabilir.")    
except ZeroDivisionError:
    print(f"Bölme hatası.")
except Exception:
    print(f"Bilinmeyen bir hata oluştu.")
