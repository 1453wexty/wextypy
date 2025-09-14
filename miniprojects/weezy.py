print("YAŞ DOĞRULAMA - 13 YAŞ ALTI DOĞRULANAMAZ")
while True:
    basla = input("Başlayalım mı? Y-N (Büyük harf küçük harf duyarlı.): ")
    if basla == "Y":
        isim = input("İsminiz: ")
        soyisim = input("Soyisminiz: ")
        yas = int(input("Yaşınız: "))

        if yas < 13:
            print("Yaşınız 13 yaşından küçük olduğu için doğrulanamadınız.")
            break
        else:
            print("Yaşınız doğrulandı.")
            break
    else:
        print("Doğrulama kullanıcı tarafından iptal edildi.")
        break