import numpy as np

def dft(signal):
    N = len(signal)
    spectrum = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        for n in range(N):
            spectrum[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)
    return spectrum

# Main program
signal = input("Masukkan sinyal (pisahkan angka dengan spasi): ")
signal = list(map(int, signal.split()))

spectrum = dft(signal)

print("Spektrum DFT:")
for k, value in enumerate(spectrum):
    print(f"Sinyal frekuensi {k}: {value}")