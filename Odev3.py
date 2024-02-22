from datetime import date, timedelta
#Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon oluşturulur.
"""def Alan_hesapla(Pi_Degeri,Yarı_cap):
   Alan_degeeri=Yarı_cap**2*Pi_Degeri
   return  Alan_degeeri
Pi_Degeri=int(input("Pi değerini giriniz "))
Yarı_cap=int(input("Yarıçap değerini giriniz "))
print("Girdiğiniz bilgilere ait dairenin alanı ",Alan_hesapla(Pi_Degeri,Yarı_cap))   """ 
"""
Faktöriyel adında fonksiyon oluşturulur. Döngü kullanarak parametre olarak girilen sayının faktöriyeli hesaplanır.
Format metodunu kullanılarak ekrana yazdırılır.
"""
"""def faktoryel(deger):
   if deger==0 and deger==1:
       return 1  
   else :
        sonuc=1
        for i in range(1,deger+1):
         sonuc*=i
        return sonuc 
     
    
sayi=int(input("Bir sayı giriniz "))
print("Girdiğiniz sayının faktörüyel değeri ",faktoryel(sayi))
"""
def yas_hesapla(dogum_yili):
  
  from datetime import date
  simdiki_yil = int(date.today().strftime("%Y"))
  return simdiki_yil - dogum_yili

def emeklilik_durumu(isim, yas_hesapla):
  yas = yas_hesapla(dogum_yili)
  emeklilik_yasi = 65
  if yas >= emeklilik_yasi:
    return f"{isim} emekli oldunuz!"
  else:
    emeklilik_kalani = emeklilik_yasi - yas
    return f"{isim} emekliliğinize {emeklilik_kalani} yıl kaldı."

# Kullanıcıdan veri alma
dogum_yili = int(input("Doğum yılınızı giriniz: "))
isim = input("Isminizi giriniz: ")

# Emeklilik durumunu hesaplama
emeklilik_durumu = emeklilik_durumu(isim, yas_hesapla)

# Sonucu yazdırma
print(emeklilik_durumu)
