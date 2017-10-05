# MeshDust-Scripts
Some scripts for a research project.  

#### fft_generated_data_test.py
Terribly named script that tries to reproduce a given number of functions through a Fourier Transform.

I had the thought to use a Fast Fourier Transform to decode a function of electrode readings by giving each some sort of "artificial frequency".

y = E1 * sin(f1 * 2pi * x) + ... + En * sin(fn * 2pi * x)

