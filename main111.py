import random

def hava_durumu_tahmin():
    """Rasgele bir hava durumu tahmini oluşturan fonksiyon."""
    durumlar = ['Güneşli', 'Parçalı Bulutlu', 'Bulutlu', 'Yağmurlu', 'Karlı']
    ruzgarlar = ['Hafif', 'Orta', 'Şiddetli']
    
    hava_durumu = random.choice(durumlar)
    ruzgar = random.choice(ruzgarlar)
    temperature = round(random.uniform(-5, 30), 2)  # -5 ile 30 arasında rastgele bir sıcaklık
    
    return {'Durum': hava_durumu, 'Rüzgar': ruzgar, 'Sıcaklık': temperature}

def ana_program():
    """Kullanıcının girdiği şehir için sahte hava durumu bilgisini ekrana yazdıran ana program."""
    print("Sahte Hava Durumu Programına Hoş Geldiniz!")
    sehir = input("Lütfen bir şehir adı girin: ")

    hava_durumu = hava_durumu_tahmin()

    print(f"\n{sehir} şehrindeki sahte hava durumu:")
    print(f"Durum: {hava_durumu['Durum']}")
    print(f"Rüzgar: {hava_durumu['Rüzgar']}")
    print(f"Sıcaklık: {hava_durumu['Sıcaklık']}°C")

# Ana programı çağır
ana_program()

