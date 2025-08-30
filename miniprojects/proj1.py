while True:
    kullanici_girdisi = input("Bir şeyler yaz: ")
    if "Değiştir" not in kullanici_girdisi:
        break
    if "Değiştir" in kullanici_girdisi:
        a = int(input("Bir sayı yaz:"))
        b = int(input("Bir sayı daha:"))
        soru = input("Toplama, Çıkarma, Çarpma, Bölme? Hangisi: ")
        if soru == "Toplama":
            print(a + b)
        if soru == "Çıkarma":
            print(a - b)
        if soru == "Çarpma":
            print(a * b)
        if soru == "Bölme":
            print(a / b)
            