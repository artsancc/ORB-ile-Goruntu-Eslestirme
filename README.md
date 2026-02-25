# ORB ile Görüntü Özellik Eşleştirme ve Görselleştirme

Bu proje, OpenCV kütüphanesini kullanarak iki görüntü arasındaki benzerlikleri saptamak için ORB algoritmasını kullanır. Algoritma, görüntülerdeki anahtar noktaları bulur, bunları tanımlar ve birbirleriyle eşleştirerek görsel bir çıktı üretir.

# Proje Özeti

Hız: 
ORB kullanarak SIFT'e göre çok daha hızlı sonuç üretir.

Verimlilik: 
İkili tanımlayıcılar sayesinde düşük bellek tüketimi sağlar.

Görselleştirme: 
Eşleşen noktaları renkli çizgilerle bağlayarak kullanıcıya sunar.

# Çalışma Mantığı

Görüntü Yükleme ve Hazırlık:
Görüntüler renkli okunur, ancak hesaplama verimliliği için uygulamaya alınmadan önce gri tonlamaya dönüştürülür.

ORB Analizi: 
ORB_create(nfeatures=1000) ile en belirgin 1000 nokta tespit edilir. Her nokta için bir descriptor oluşturulur.

Brute-Force Eşleştirme: 
BFMatcher ile iki görüntüdeki noktalar kıyaslanır. ORB ikili bir sistem olduğu için NORM_HAMMING (bit farkı ölçümü) kullanılır.

Sıralama ve Filtreleme: 
Bulunan tüm eşleşmeler en yakından en uzağa doğru sıralanır. Sadece en kaliteli ilk 50 eşleşme seçilir.

Boyutlandırma:
Yüksek çözünürlüklü çıktıların ekrana sığması için görüntü %60 oranında küçültülür.

#Input

![img1](https://github.com/user-attachments/assets/57596d45-e63e-4383-84e9-6f934e3a1936)
![img2](https://github.com/user-attachments/assets/08bce57e-e045-4aa3-a04b-88401434b40c)

#Output

![sonuc](https://github.com/user-attachments/assets/1d811597-810e-450c-af3b-9d2a77667042)

# Sonuç

Bu uygulama sonucunda elde edilen çizgiler, iki görüntü arasındaki fiziksel karşılıkları temsil eder. 



