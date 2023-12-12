import time
izlenecek_filmler=["Karayip Korsanlari", "Wonder", "Ice Age", "Finding Dory"]
while True:
    print("Kullanabileceğiniz komutlar: yazdir, ekle, sil, çikiş")
    komut=input("Ne yapmak istersiniz?: ")
    if komut=="yazdir":
        for film in izlenecek_filmler:
            print(film)
            time.sleep(1)
    elif komut=="ekle":
        yeni_film=input("Listeye hangi filmi eklemek istersiniz?: ")
        izlenecek_filmler.append(yeni_film)
        print("Yeni film listenize ekleniyor...")
        time.sleep(1)
        print("Yeni film listenize eklendi!")
        time.sleep(1)
    elif komut=="sil":
        izlenen_film=input("Listeden hangi filmi silmek istersiniz?: ")
        izlenecek_filmler.remove(izlenen_film)
        print("Film listenizden çikariliyor...")
        time.sleep(1)
        print("Film listenizden çikarildi!")
        time.sleep(1)
    elif komut=="çikiş":
        print("Listeniz kaydediliyor...")
        time.sleep(1)
        print("Yeni listeniz başariyla kaydedildi, görüşmek üzere!")
        time.sleep(1)
        break
    else:
        print("Geçerli bir giriş yapmadiniz, lütfen cevabinizi kontrol ediniz.")
        time.sleep(1)