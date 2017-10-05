import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt


# Number of sample points
N = 50

# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y1 = np.sin(50*2*np.pi*x)
y2 = np.sin(80*2*np.pi*x)
y = 1*np.sin(50.0 * 2.0*np.pi*x) + 1*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
print xf.shape
print yf.shape
print len(2.0/N * np.abs(yf[0:N//2]))

# Me
#plt.plot(x, y1)
#plt.plot(x, y2)

# Plot
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()