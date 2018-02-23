# MeshDust-Scripts
Some scripts for a research project.  

#### fft_generated_data_test.py
Reproduce a given number of time series through a Fourier Transform.

I had the thought to use a Fast Fourier Transform to decode a function of electrode readings by giving each some sort of "artificial frequency".  In other words, map the time series of each electrode to the amplitude of a wave of a distinct frequency.  By doing so, you can add up the signals and have only one channel to read from.

y = E1 * sin(f1 * 2pi * x) + ... + En * sin(fn * 2pi * x)

