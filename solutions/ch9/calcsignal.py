import numpy as np

def dft(s):
    """Computes the discrete Fourier transform of a signal"""
    # Create the DFT matrix
    N = len(s)
    y_N = np.exp(1j * 2 * np.pi / N)
    k = np.arange(N)
    n = np.arange(N)
    kn = np.outer(k, n)
    Y = y_N ** kn
    # Compute the DFT
    s_hat = Y @ s
    return s_hat

def fft(s):
    """Computes the discrete Fourier transform of a signal using a FFT"""
    N = len(s)
    if N == 1:
        return s
    else:
        # Recursively compute the DFT on each half of the signal
        a = fft(s[0::2])
        b = fft(s[1::2])
        # Compute the twiddle factors and twiddle
        y_N = np.exp(1j * 2 * np.pi / N)
        k = np.arange(N // 2)
        c = (y_N ** k) * b
        # Compute the DFT
        s_hat = np.zeros(N, dtype=np.complex128)
        s_hat[0:N // 2] = a + c
        s_hat[N // 2:N] = a - c
        return s_hat
