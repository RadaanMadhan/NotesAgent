# Modulation Cheat Sheet

## Formulae

### 1. Modulation of Baseband to Passband
- **Cosine Modulation:**
  
  \[
  u_p(t) = m(t) \cos(2\pi f_c t)
  \]
  
  Frequency domain representation:
  
  \[
  U_p(f) = \frac{1}{2}[M(f-f_c) + M(f+f_c)]
  \]
  
- **Sine Modulation:**
  
  \[
  v_p(t) = m(t) \sin(2\pi f_c t)
  \]
  
  Frequency domain representation:
  
  \[
  V_p(f) = \frac{1}{2j}[M(f-f_c) - M(f+f_c)]
  \]

### 2. In-phase and Quadrature Components (I/Q Modulation)

\[
  u(t) = u_I(t) \cos(2\pi f_c t) - u_Q(t) \sin(2\pi f_c t)
\]

### 3. Quadrature Amplitude Modulation (QAM)

\[
  s(t) = u_I(t) \cos(2\pi f_c t) - u_Q(t) \sin(2\pi f_c t)
\]

### 4. Signal-to-Noise Ratio (SNR) 

- **Energy per bit to noise power spectral density ratio:**
  
  \[
  \text{SNR}_e = Q\left(\sqrt{\frac{E_b}{N_0}}\right)
  \]
  
- **SNR in decibels:**
  
  \[
  \text{SNR (dB)} = 6n + 10 \log_{10} \left(\frac{3P_p}{m_2}\right)
  \]

### 5. Coherent Detection of QAM

\[
  x(t) = s(t) + n(t) = u_I(t)\cos(2\pi f_c t) - u_Q(t)\sin(2\pi f_c t) + n(t)
\]

## Concepts

### Modulation of Baseband to Passband
This process involves translating a baseband signal, `m(t)`, which has a limited frequency range (bandwidth `W`), to a passband signal. This is crucial for frequency-division multiplexing and efficient signal transmission over various media. `f_c` is the carrier frequency, which is higher than the message signal's bandwidth. Modulation shifts the baseband frequency spectrum to the passband frequencies centered around the carrier frequency.

### In-phase and Quadrature Components (I/Q Modulation)
I/Q modulation is a method that uses two carriers, typically cosine for in-phase and sine for quadrature, to modulate a signal. `u_I(t)` and `u_Q(t)` are the in-phase and quadrature components, respectively, allowing the modulation of both amplitude and phase of the carrier signal, essential for digital communication methods like QAM.

### Quadrature Amplitude Modulation (QAM)
QAM is a modulation technique that combines both amplitude and phase variations. The QAM concept extends I/Q modulation by enabling multiple amplitude and phase combinations, which increases the data rate. Amplitude Shift Keying (ASK) and Phase Shift Keying (PSK) are simpler forms of QAM. It is commonly used in modern wireless and digital TV systems for its efficiency.

### Signal-to-Noise Ratio (SNR) and Performance
SNR is critical for assessing the quality of modulation systems in noisy environments. `E_b` is the energy per bit and `N_0` the noise power density. The `Q` function is the tail of the normal distribution, used in error calculation. In practical assessments, higher SNR indicates better performance.

### Coherent Detection of QAM
Coherent detection involves demodulating the received QAM signal using knowledge of the carrier's phase. `n(t)` is the noise present in the channel. Coherent detection requires phase synchronization between transmitter and receiver, enabling accurate demodulation and retrieval of the original signal components.

These concepts are fundamental for understanding how modulation processes work to convey information efficiently across communication systems. They allow engineers to design and analyze systems for a variety of applications from radios to modern data networks.