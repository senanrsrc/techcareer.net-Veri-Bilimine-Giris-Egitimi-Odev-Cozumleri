""" 1. Kullanicidan adını, yaşını ve boyunu (float) input() ile alınız.
Bu bilgileri uygun veri tiplerinde değişkenlerde saklayınız ve ekrana anlamlı bir şekilde yazdırınız."""

ad = input("Ad giriniz: ").capitalize()
yas = int(input("Yaş giriniz: "))
boy = float(input("Boyunuzu giriniz (metre cinsinden): "))
print( f"Ad: {ad}, Yaş: {yas}, Boy: {boy}" )


"""2. Bir öğrencinin notlarını (Matematik, Fizik, Kimya) int tipinde değişkenlere atayın. Ortalamasını 
float tipinde hesaplayıp ekrana yazdırınız."""
matematik_notu = int(input("Matematik notunu giriniz:"))
fizik_notu = int(input("Fizik notunu giriniz:"))
kimya_notu = int(input("Kimya notunu giriniz:"))
ortalama = float((matematik_notu + fizik_notu + kimya_notu) / 3.0)
print(f"Ortalama:{ortalama}")


"""3. Bir string değişkeni tanımlayın. Bu stringin ilk ve son karakterini, uzunluğunu ve ters çevrilmiş 
halini ekrana yazdırınız."""

string = "senanur"
ilk_karakter = string[0]
son_karakter = string[-1]
uzunluk = len(string)
ters_cevrilmis = string[::-1]
print(f"İlk karakter: {ilk_karakter}, Son karakter: {son_karakter}, "
      f"Uzunluk: {uzunluk}, Ters çevrilmiş: {ters_cevrilmis}")


"""4. Kullanıcıdan iki sayı alınız. Bu sayılar üzerinde toplama, çıkarma, çarpma, bölme ve mod işlemleri yapınız."""
sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))
toplam = sayi1 + sayi2
cikarma = sayi1 - sayi2
carpma = sayi1 * sayi2
if sayi2 != 0 :
	bolme = sayi1 / sayi2
	mod = sayi1 % sayi2
else:
	bolme = "Bölme işlemi için ikinci sayı sıfır olamaz"
	mod = "Mod işlemi için ikinci sayı sıfır olamaz"
print(f"Toplam: {toplam}, Çıkarma: {cikarma}, Çarpma: {carpma}, Bölme: {bolme}, Mod: {mod}")



"""5. Bir öğrencinin ortalaması 50’den büyükse 'Geçti', değilse 'Kaldı' çıktısını veren bir program yazınız. 
(Karşılaştırma ve mantıksal operatörler kullanılacak.)"""
ortalama = float(input("Öğrencinin ortalamasını giriniz: "))
if ortalama > 50:
	print("Geçti")
else:
	print("Kaldı")



"""6. Kullanıcıdan yaşını alınız. Eğer yaş 18’den büyükse 'Ehliyet alabilirsiniz', değilse 
'Ehliyet alamazsınız' çıktısı veriniz."""
yas = int(input("Yaşınızı giriniz: "))
if yas >= 18:
	print("Ehliyet alabilirsiniz")
else:
	print("Ehliyet alamazsınız")


"""7. Bir ürünün fiyatını (float) ve indirim oranını (yüzde) alınız. İndirimli fiyatı hesaplayıp 
ekrana yazdırınız. (Aritmetik operatörler kullanılacak.)"""
urun_fiyati = float(input("Ürünün fiyatını giriniz: "))
indirim_orani = float(input("İndirim oranını yüzde olarak giriniz: "))
indirimli_fiyat = urun_fiyati - (urun_fiyati * (indirim_orani / 100))
print(f"İndirimli fiyat: {indirimli_fiyat}")


"""8. True ve False değerlerini içeren değişkenlerle mantıksal operatörleri (and, or, not) uygulayarak örnekler 
yapınız ve sonuçlarını ekrana yazdırınız."""
true_deger = True
false_deger = False
and_sonuc = true_deger and false_deger
or_sonuc = true_deger or false_deger
not_sonuc = not true_deger
print(f"True and False: {and_sonuc}, True or False: {or_sonuc}, not True: {not_sonuc}")


"""9. Küçük bir alışveriş sepeti uygulaması yapınız: - Kullanıcıdan 3 ürünün fiyatını alınız. 
- Toplam fiyatı hesaplayınız. 
- Eğer toplam fiyat 200 TL’den fazlaysa %10 indirim uygulayınız. 
- Son fiyatı ekrana yazdırınız."""
urun1_fiyat = float(input("1. ürünün fiyatını giriniz: "))
urun2_fiyat = float(input("2. ürünün fiyatını giriniz: "))
urun3_fiyat = float(input("3. ürünün fiyatını giriniz: "))
toplam_fiyat = urun1_fiyat + urun2_fiyat + urun3_fiyat
if toplam_fiyat > 200:
	indirim = toplam_fiyat * 0.10
	son_fiyat = toplam_fiyat - indirim
else:
	son_fiyat = toplam_fiyat
print(f"Toplam fiyat: {toplam_fiyat}, Son fiyat: {son_fiyat}")

"""10.Kullanıcıdan doğum yılını alınız. Bu yıl ile güncel yılı kullanarak yaşını hesaplayınız. 
Yaşına göre şu mesajlardan birini veriniz: 
- 0-12: 'Çocuksunuz' - 13-17: 'Ergensiniz' - 18 ve üzeri: 'Yetişkinsiniz'  """
dogum_yili = int(input("Doğum yılınızı giriniz: "))
guncel_yil = 2025
yas = guncel_yil - dogum_yili
if yas < 0:
	print("Doğum yılınız gelecekte olamaz!")
elif yas <= 12:
	print("Çocuksunuz")
elif yas <= 17:
	print("Ergensiniz")
elif yas >= 18:
	print("Yetişkinsiniz")