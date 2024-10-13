import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Video dosyasını açma
videoyolu = 'onemli3.mp4'
cap = cv2.VideoCapture(videoyolu)

# Hareketleri kaydetme listesi
motionlistesi = []
fps = cap.get(cv2.CAP_PROP_FPS)

# İlk kareyi kaydetme
ilkkare = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # gri tonlama daha iyi işleyebilmek için
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Gaussian Blur uygulama
    blurla = cv2.GaussianBlur(gray, (101, 101), 0)
    
    # İlk kareyi saklama
    if ilkkare is None:
        ilkkare = blurla
        continue
    
    # İlk kare ile mevcut kare arasındaki fark
    harekettespiti = cv2.absdiff(ilkkare, blurla)
    
    # Threshold uygulama
    thresh = cv2.threshold(harekettespiti, 10, 255, cv2.THRESH_BINARY)[1]
    
    # Hareket miktarını listeye ekleme
    motionlistesi.append(np.sum(thresh))

# Videoyu kapatma
cap.release()

# FFT hesaplama
fft_values = fft(motionlistesi)
fft_freqs = fftfreq(len(motionlistesi), 1.0 / fps)

# FFT genliklerinin düzeltilmesi (örnekleme sayısına bölüp ikiye böleceğiz)
genlik = (2.0 / len(motionlistesi)) * np.abs(fft_values)

# Pozitif frekans bileşenlerini alalım
pozitif_freqs = fft_freqs[:len(fft_freqs)//2]
pozitif_genlikler = genlik[:len(genlik)//2]

# İki grafiği tek figürde çizme
plt.figure(figsize=(12, 12))

# Hareket miktarı grafiği
plt.subplot(2, 1, 1)  # 2 satır, 1 sütun, 1. grafik
plt.plot(motionlistesi, label="Hareket Miktarı")
plt.title("Hareket Miktarı Grafiği")
plt.xlabel("Kare Sayısı")
plt.ylabel("Hareket Miktarı")
plt.legend()
plt.grid()

# FFT grafiği (pozitif frekanslar)
plt.subplot(2, 1, 2)  # 2 satır, 1 sütun, 2. grafik
plt.plot(pozitif_freqs, pozitif_genlikler)
plt.title('FFT (Frekans Bileşenleri)')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.grid()

# Grafikleri yerleşim düzenine göre sıkıştırma
plt.tight_layout()
plt.show()
