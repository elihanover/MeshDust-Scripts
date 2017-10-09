import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

"""

Next:
- Figure out why d-FFT values make NO sense
- Try with some noise, shouldn't do anything catastrophic
- Run this with some real sensory data or fake spike data
- Update based on timing parameters of dust

"""


##### Generate Fake PD Data #####
# These would be TUNED
S = 100 # sample window size (Fft freq = 1/(T*S) Hz
N = 500000 # Number of sample points, arbitrarily chosen
T = 1.0 / 1000.0 # freq of recording 1 kHz (from Syringe-injectable electronics paper)

# Entire time-signal
x = np.linspace(0.0, N*T, N)

# Stupid electrode readings to experiment with
e1 = 10*np.sin(.5*2*np.pi*x)+50 # <-- doesn't seem to work well with sin data
e2 = np.sin(.00008*2*np.pi*x) #   for some reason creates a valley here with two peaks surrounding it...why though?
e3 = 0.4*x + 3 # some line
e4 = 2*x + 6 # some negative line
e5 = (x-6)**2 # some parabola



# Artificial Frequencies
af1 = 100
af2 = 200
af3 = 300
af4 = 400
# Should sample at multiple of frequency so that it's a complete cycle

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
y = e1 * np.sin(af1 * 2 * np.pi * x) + e4 * np.sin(af2 * 2 * np.pi * x)
#y = np.sin(af1 * 2 * np.pi * x) + np.sin(af2 * 2 * np.pi * x)

# FFT Plot Data
y1 = [] # V's at 40 Hz
y2 = [] # V's at 80 Hz
y3 = []
y4 = []

for i in range(0, N, S): # assumes N%10 == 0
    xf = np.linspace(0.0, 1.0/(2.0*T), S//2)
    print "len XF", len(xf)

    # Fast Fourier Transform
    yf = fft(y[i:i+S])
    yf = 2.0/S * np.abs(yf[0:S//2])
    print len(yf)
    # Get V values at each artificial frequency

    # TODO: calculate these values programmatically, besides the point for now


    y1.append(yf[10]) # get V value at af1
    y2.append(yf[20]) # get V value at af2

    print y1[-1], y2[-1]
    
    #y1.append(yf[0])
    #y2.append(yf[1])
    

    #y3.append(yf[16])
    #y4.append(yf[21])

    if i < S*4:
      plt.plot(xf, yf, 'xr')
      plt.grid()
      plt.show()


##### PLOT #####
t = [i*S*T for i in range(N/S)] # x-axis of plot d-FFT is time
plt.plot(t, y1, "r") # plot d-FFT
plt.plot(t, y2, "g") # <--- The values aren't the same
#plt.plot(X, y3, "b")
#plt.plot(X, y4, "y")
plt.grid()
plt.show()
