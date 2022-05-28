sayi1 = int(input("1. sayıyı girin: "))
sayi2 = int(input("2. sayıyı girin: "))
islem = input("Toplama için (+) Çıkarma için (-) Çarpım(*) Bölme(/) girin")

if islem == "+":
    sonuc = sayi1 + sayi2
    print("Toplamı:",sonuc)
elif islem == "-":
    sonuc = sayi1 - sayi2
    print("Farkı:",sonuc)
elif islem == "*":
    sonuc = sayi1 * sayi2
    print("Çarpım",sonuc)
elif islem == "/":
    sonuc = sayi1 / sayi2
    print("Bölüm",sonuc)
else:
    print("Hatalısınız! \nAma üzülmeyin hatasız kul olmaz.")
