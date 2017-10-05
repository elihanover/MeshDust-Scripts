import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

"""

Next:
Try with some noise, shouldn't do anything catastrophic
Run this with some real sensory data
or fake spike data

"""


##### Generate Fake PD Data #####
# These would be TUNED
S = 100 # Sampling rate of fft, 20 mHz
N = 500 # Number of sample points, arbitrarily chosen
T = 1.0 / 1000.0 # freq of recording 1 kHz (from Syringe-injectable electronics paper)

# Entire time-signal
x = np.linspace(0.0, N*T, N)

# Stupid electrode readings to experiment with
e1 = np.sin(.00005*2*np.pi*x) # <-- doesn't seem to work well with sin data
e2 = np.sin(.00008*2*np.pi*x) #   for some reason creates a valley here with two peaks surrounding it...why though?
e3 = 0.4*x + 3 # some line
e4 = -0.3*x + 6 # some negative line
e5 = (x-6)**2 # some parabola



# Artificial Frequencies
af1 = 100
af2 = 200
af3 = 300
af4 = 400


# Smush electrode data with artificial frequencies
"""
  y = sum(Ai * sin(fi * 2pi * x))
  If A (voltage) values are not taken in one moment in time, are they averages?
  This can be a problem for sine values if the sin freq is higher than the sampling freq
    >> Means that the values average out to zero
  In short, need averages to make sense no matter the function
  	>> Should be fine for voltage since spikes should be noticed either way
"""
#y = e3 * np.sin(af1 * 2 * np.pi * x) + e4 * np.sin(af2 * 2 * np.pi * x) + e3 * np.sin(af3 * 2 * np.pi * x) + e4 * np.sin(af4 * 2 * np.pi * x)
y = e3 * np.sin(af1 * 2 * np.pi * x) + e4 * np.sin(af2 * 2 * np.pi * x)
#xf = np.linspace(0.0, 1.0/(2.0*T), N//2)


# FFT Plot Data
y1 = [] # V's at 40 Hz
y2 = [] # V's at 80 Hz
#print xf[0]

for i in range(0, N, S): # assumes N%10 == 0
	xf = np.linspace(0.0, 1.0/(2.0*T), S//2)
	print "i:", i

    # Fast Fourier Transform
    yf = fft(y[i:i+S])

    # Get V values at 
	# need to map xf value onto yf
	y1.append(yf[af1]) # get V value at af1
	y2.append(yf[af2]) # get V value at af2
	print "yf:", yf
	print "thing:", (2.0/S * np.abs(yf[i//2:(i+S)//2])) # <-- need to sort out why this breaks
	print "shape", (2.0/S * np.abs(yf[i//2:(i+S)//2])).shape
	plt.plot(xf, 2.0/S * np.abs(yf[0:S//2]))
	plt.grid()
	plt.show() # <--- why are readings so bad


# Plot
#plt.plot(xf, 2.0/N * np.abs(yf[0:N//2])) # plot FFT
#plt.plot(x, y1) # plot d-FFT
#plt.grid()
#plt.show()

"""
Need to take this and figure out how to monitor
electrode readings with time.

I.E. How do I get back the input function from FFT?

Take FFT at 1 kHz frequency...

"""
