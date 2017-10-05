# MeshDust-Scripts
Some scripts for a research project.  

#### fft_generated_data_test.py
Terribly named script that tries to reproduce a given number of functions through a Fourier Transform.
I had the thought to use a Fast Fourier Transform to decode summed electrode readings by giving each some sort of "artificial frequency".

We can run a FFT on
y = A1 * sin(f1 * 2 * \Pi * x) + ... + An * sin(fn * 2 * \Pi * x)
