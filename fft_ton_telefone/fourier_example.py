import scipy.io as sio
import matplotlib.pyplot as plt

import numpy as np
arq = 'toque.wav'
fs, data = sio.wavfile.read(arq)
data = data.sum(1)
print(data.shape[0])
data
t = np.arange(0,data.shape[0])/fs
plt.plot(t,data)
sel1 = (t>6) & (t<6.3)
t1 = t[sel1]
s1 = data[sel1]

s1_fft = np.fft.fft(s1)
s1_abs = np.absolute(s1_fft)
freqs = np.linspace(0,1,s1.shape[0])*fs
plt.plot(freqs,s1_abs)
