import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Parametreler
sampling_rate = 1000  # örnekleme frekansı (Hz)
T = 1.0 / sampling_rate  # zaman aralığı
t = np.arange(0, 1.0, T)  # 1 saniyelik zaman aralığı

# Sinyaller: 50 Hz ve 120 Hz sinyalleri
signal_50hz = 3 * np.sin(2 * np.pi * 50 * t)  # 50 Hz'lik sinyal
signal_120hz = 5 * np.sin(2 * np.pi * 120 * t)  # 120 Hz'lik sinyal

# Orijinal fonksiyon (elle yazılmış)
original_signal = 3 * np.sin(2 * np.pi * 50 * t) + 5 * np.sin(2 * np.pi * 120 * t)

# FFT hesaplaması (Toplam sinyal için)
fft_values = fft(original_signal)
fft_freqs = fftfreq(len(t), T)

# FFT genliklerinin düzeltilmesi (Örnekleme sayısına bölüp ikiye böleceğiz)
genlik = (2.0 / len(t)) * np.abs(fft_values)  # Genlikleri normalize etmek

# Grafikleri çizme
plt.figure(figsize=(10, 12))

# Orijinal fonksiyon (elle yazılmış)
plt.subplot(5, 1, 1)
plt.plot(t, original_signal, label='Orijinal Fonksiyon (3sin(2π50t) + 5sin(2π120t))', color='orange')
plt.title('Orijinal Fonksiyon')
plt.xlabel('Zaman (saniye)')
plt.ylabel('Genlik')
plt.grid(True)
plt.legend()

# 50 Hz sinyali
plt.subplot(5, 1, 2)
plt.plot(t, signal_50hz, label='50 Hz Sinyali', color='b')
plt.title('50 Hz Sinyali (Genlik: 3)')
plt.xlabel('Zaman (saniye)')
plt.ylabel('Genlik')
plt.grid(True)
plt.legend()

# 120 Hz sinyali
plt.subplot(5, 1, 3)
plt.plot(t, signal_120hz, label='120 Hz Sinyali', color='r')
plt.title('120 Hz Sinyali (Genlik: 5)')
plt.xlabel('Zaman (saniye)')
plt.ylabel('Genlik')
plt.grid(True)
plt.legend()

# Toplam sinyal (50 Hz + 120 Hz)
plt.subplot(5, 1, 4)
plt.plot(t, original_signal, label='Toplam Sinyal (50 Hz + 120 Hz)', color='g')
plt.title('Toplam Sinyal (50 Hz + 120 Hz)')
plt.xlabel('Zaman (saniye)')
plt.ylabel('Genlik')
plt.grid(True)
plt.legend()

# FFT grafiği (Frekans bileşenleri)
plt.subplot(5, 1, 5)
plt.plot(fft_freqs[:len(t)//2], genlik[:len(genlik)//2], label='FFT Genlikleri', color='purple')
plt.title('FFT (Frekans Bileşenleri)')
plt.xlim(0, 200)  # Sadece pozitif frekansları gösterelim
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
