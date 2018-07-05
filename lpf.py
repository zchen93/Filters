# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 21:30:32 2018

@author: Zengweijie (Fred) Chen

Frequency Response Plot
Low-Pass Filter
"""

from pylab import *

fc = 4000
K = 1
f = logspace(1,5) # frequencies from 10^1 to 10^5

def H(w, K, wc):

   H = K / (1.0 + 1j * w / wc)
   return H

H_log = 20*log10(abs(H(2*pi*f, K, 2*pi*fc)))

# Plotting Configuration
figure(num = 3, figsize = (16, 12), dpi = 100, facecolor='w', edgecolor='k')
plot(f, H_log)
xscale('log')
title(r'Unity-Gain LPF Frequency Response, $f_{3dB}$ = %s Hz' %fc)
xlabel('Frequency [Hz]')
ylabel('Gain [dB]')
grid(True)

savefig('LPF.png')