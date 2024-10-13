import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Parametreler
sampling_rate = 1000  # örnekleme frekansı (Hz)
T = 1.0 / sampling_rate  # zaman aralığı
t = np.arange(0, 1.0, T)  # 1 saniyelik zaman aralığı

# f(t) fonksiyonunun tanımlanması
f_t = 2 * np.sin(2 * np.pi * 30 * t) + 1.5 * np.sin(2 * np.pi * 60 * t) + 1.0 * np.sin(2 * np.pi * 90 * t) + 0.5 * np.sin(2 * np.pi * 150 * t) + 0.8 * np.sin(2 * np.pi * 200 * t)


# Farklı frekanslardaki sinyallerin tanımlanması
signal_30hz = 2 * np.sin(2 * np.pi * 30 * t)   # 30 Hz'lik sinyal, genlik 2
signal_60hz = 1.5 * np.sin(2 * np.pi * 60 * t)  # 60 Hz'lik sinyal, genlik 1.5
signal_90hz = 1.0 * np.sin(2 * np.pi * 90 * t)  # 90 Hz'lik sinyal, genlik 1
signal_150hz = 0.5 * np.sin(2 * np.pi * 150 * t)  # 150 Hz'lik sinyal, genlik 0.5
signal_200hz = 0.8 * np.sin(2 * np.pi * 200 * t)  # 200 Hz'lik sinyal, genlik 0.8

# Toplam sinyal: Tüm sinyallerin birleşimi
total_signal = signal_30hz + signal_60hz + signal_90hz + signal_150hz + signal_200hz

# Orijinal fonksiyon (toplam sinyal ile aynı)
original_signal = total_signal

# FFT hesaplaması (Toplam sinyal için)
fft_values = fft(total_signal)
fft_freqs = fftfreq(len(t), T)

# FFT genliklerinin düzeltilmesi (Örnekleme sayısına bölüp ikiye böleceğiz)
genlik = (2.0 / len(t)) * np.abs(fft_values)  # Genlikleri normalize etmek

# Grafikleri çizme
plt.figure(figsize=(12, 16))


# Orijinal fonksiyon 
plt.subplot(8, 1, 1)
plt.plot(t, f_t, label='f(t)', color='orange' )
plt.title('Orijinal fonksiyon')
plt.xlabel('Zaman (saniye)')
plt.ylabel('Genlik')
plt.grid(True)
plt.legend()
plt.show()


# 30 Hz sinyali
plt.subplot(8, 1, 2)
plt.plot(t, signal_30hz, label='30 Hz Sinyali', color='b')
plt.title('30 Hz Sinyali (Genlik: 2)')
plt.xlabel('Zaman (saniye)')
plt.ylabel('Genlik')
plt.grid(True)
plt.legend()

# 60 Hz sinyali
plt.subplot(8, 1, 3)
plt.plot(t, signal_60hz, label='60 Hz Sinyali', color='r')
plt.title('60 Hz Sinyali (Genlik: 1.5)')
plt.xlabel('Zaman (saniye)')
plt.ylabel('Genlik')
plt.grid(True)
plt.legend()

# 90 Hz sinyali
plt.subplot(8, 1, 4)
plt.plot(t, signal_90hz, label='90 Hz Sinyali', color='g')
plt.title('90 Hz Sinyali (Genlik: 1)')
plt.xlabel('Zaman (saniye)')
plt.ylabel('Genlik')
plt.grid(True)
plt.legend()

# 150 Hz sinyali
plt.subplot(8, 1, 5)
plt.plot(t, signal_150hz, label='150 Hz Sinyali', color='purple')
plt.title('150 Hz Sinyali (Genlik: 0.5)')
plt.xlabel('Zaman (saniye)')
plt.ylabel('Genlik')
plt.grid(True)
plt.legend()

# 200 Hz sinyali
plt.subplot(8, 1, 6)
plt.plot(t, signal_200hz, label='200 Hz Sinyali', color='orange')
plt.title('200 Hz Sinyali (Genlik: 0.8)')
plt.xlabel('Zaman (saniye)')
plt.ylabel('Genlik')
plt.grid(True)
plt.legend()

# Toplam sinyal (Birleşim)
plt.subplot(8, 1, 7)
plt.plot(t, total_signal, label='Toplam Sinyal (Tüm Frekanslar)', color='black')
plt.title('Toplam Sinyal (30 Hz + 60 Hz + 90 Hz + 150 Hz + 200 Hz)')
plt.xlabel('Zaman (saniye)')
plt.ylabel('Genlik')
plt.grid(True)
plt.legend()

# FFT grafiği (Frekans bileşenleri)
plt.subplot(8, 1, 8)
plt.plot(fft_freqs[:len(t)//2], genlik[:len(t)//2], label='FFT Genlikleri', color='purple')
plt.title('FFT (Frekans Bileşenleri)')
plt.xlim(0, 250)  # Sadece pozitif frekansları gösterelim
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
