# 1. Kullanıcıya gizemli bir soru sorun
gizemli_soru = input("Eğer bir ejderha olsaydınız, adınız ne olurdu? ")

# 2. Kullanıcının cevabını ilginç bir şekilde karşılayın
print("Ah, " + gizemli_soru.capitalize() + "! Harika bir ejderha adı seçtiniz!")

# 3. Kullanıcıdan bir pozitif sayı alın
pozitif_sayi = int(input("Bana pozitif bir sayı verin: "))

# 4. Sayıyı iki katına çıkarın
sonuc = pozitif_sayi * 2

# 5. Sonucu ekrana renkli bir şekilde yazdırın
print("\033[1;32;40mİki katı:", sonuc)
