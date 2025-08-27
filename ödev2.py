
################### Soru 1 – Sayı Analizi ###################

sayi = int(input("Lütfen bir sayı girin:"))

if sayi > 0:
    sayidurumu = "pozitif"
elif sayi < 0:
    sayidurumu = "negatif"
else:
    sayidurumu = "sıfır"

if sayi % 2 == 0:
    teklikciftlik = "çift"
else:
    teklikciftlik = "tek"

print(sayi, ":" , sayidurumu, teklikciftlik)

################### Soru 2 – Harf Frekansı ###################
kelime = input("Lütfen bir kelime girin:")
frekans = {}

for harf in kelime:
    if harf in frekans:
        frekans[harf] += 1
    else:
        frekans[harf] = 1

print(f"{kelime} kelimesinin harf frekansı: {frekans}")


 ################### Soru 3 – Şifre Kontrolü ###################

sifre = input("Lütfen oluşturmak istediğiniz şifreyi girin: ")

buyuk_harf_kontrolu = False
rakam_kontrolu = False

for karakter in sifre:
    if karakter.isupper():
        buyuk_harf_kontrolu = True
    if karakter.isdigit():
        rakam_kontrolu = True

if len(sifre) >= 8 and buyuk_harf_kontrolu and rakam_kontrolu:
    print("Şifreniz geçerli, başarıyla oluşturuldu.")
else:
    print("Şifre kurallara uymuyor, lütfen tekrar deneyiniz.")


################### Soru 4 – Liste İşlemleri ###################
sayilar = [12, 4, 9, 25, 30, 7, 18]

toplam = 0
for s in sayilar:
    toplam += s

ortalama = toplam / len(sayilar)

ortdan_buyuk = []
for s in sayilar:
    if s > ortalama:
        ortdan_buyuk.append(s)

print("Ortalama:", ortalama)
print("Ortalamadan büyük sayılar:", ortdan_buyuk)


################### Soru 5 – Nested Loop (Desen) ###################

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()


################### Soru 6 – While Döngüsü ###################
toplam = 0
adet = 0

while True:
    sayi = int(input("Lütfen istediğiniz sayıyı girin (Çıkmak istediğinizde 0'a basın!) :"))
    if sayi == 0:
        break
    toplam += sayi
    adet += 1

if adet > 0:
    print("Sayılarınızın Toplamı:", toplam)
    print("Sayılarınızın Ortalaması:", toplam / adet)
else:
    print("Hiç sayı girmediniz.")

 ################### Soru 7 – Palindrom Kontrolü ###################

kelime = input("Bir kelime girin: ")

if kelime == kelime[::-1]:
    print(f"{kelime} kelimesi palindrom.")
else:
    print(f"{kelime} kelimesi palindrom değil.")

################### Soru 8 – List Comprehension ###################
liste = []
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        liste.append(x**2)

print("1’den 100’e kadar olan sayılardan hem 3’e hem 5’e bölünebilenlerin kareleri:" , liste)

################### Soru 9 – String İşlemleri ###################
cumle = input("Lütfen cümlenizi girin: ")
kelimeler = cumle.split()

yeni_cumle = ""
for k in kelimeler:
    yeni_cumle += k.capitalize() + " "

print(yeni_cumle.strip())



################### Mini Proje – Film Yorumu Analizi ###################
yorumlar = []
adet = int(input("Kaç adet yorum gireceksiniz? "))

for i in range(adet):
    yorum = input(f"{i+1}. yorumu girin: ")
    yorumlar.append(yorum)

# 1. Uzunlukları hesaplama
uzunluklar = []
for y in yorumlar:
    uzunluklar.append(len(y))

# 2. "iyi" geçen yorum sayısı
iyi_sayisi = 0
for y in yorumlar:
    if "iyi" in y.lower():   # küçük harfe çevirerek arıyoruz
        iyi_sayisi += 1

# 3. En uzun ve en kısa
en_uzun = yorumlar[0]
en_kisa = yorumlar[0]
for y in yorumlar:
    if len(y) > len(en_uzun):
        en_uzun = y
    if len(y) < len(en_kisa):
        en_kisa = y

# 4. Ortalama uzunluk
toplam_uzunluk = 0
for u in uzunluklar:
    toplam_uzunluk += u
ortalama_uzunluk = toplam_uzunluk / len(uzunluklar)

print("Toplam yorum sayısı:", len(yorumlar))
print('"iyi" geçen yorum sayısı:', iyi_sayisi)
print("En uzun yorum:", en_uzun)
print("En kısa yorum:", en_kisa)
print("Yorumların ortalama uzunluğu:", ortalama_uzunluk, "karakter")

