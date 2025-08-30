print("NOT ORTALAMASI BULUCU")
while True:
    kullanici_baslangic = input("Başlayalım mı? ")
    if kullanici_baslangic == "Başlayalım":
        matematik = float(input("Matematik Notunu Gir: "))
        fizik = float(input("Fizik Notunu Gir: "))
        kimya = float(input("Kimya Notunu Gir: "))
        biyoloji = float(input("Biyoloji Notunu Gir: "))
        edebiyat = float(input("Edebiyat Notunu Gir: "))
        ingilizce = float(input("İngilizce Notunu Gir: "))
        sonuc = (matematik + fizik + kimya + biyoloji + edebiyat + ingilizce) / 6
        if sonuc > 50:
            print(sonuc)
            print("Sınıfı Geçtin.")
        else:
            print(sonuc)
            print("Sınıfı Geçemedin.")
    else:
        break
print("Programdan çıkılıyor...")