# try:
#   yapılacak işlemler:
# expect ValueError:
#   alınan hatanın yönetimi

# örn:

try:
    telefon_no = input("Telefon no: ")
    sayi_telefon_no = int(telefon_no)
    print(f"Telefon no: {sayi_telefon_no}")
except ValueError as e:
    print(f"Lütfen telefon numarasını sayı olarak doğru bir şekilde girin! ")
    print(f"Hatanız : {e}")






