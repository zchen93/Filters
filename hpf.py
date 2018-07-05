# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 22:02:29 2018

@author: Zengweijie (Fred) Chen

Frequency Response Plot
High-Pass Filter
""" 

from pylab import *

fc = 4000
K = 1
f = logspace(1,6) # frequencies from 10^1 to 10^5

def H(w, K, wc):

   H = K* 1j *w / (wc + 1j*w)
   return H

H_log = 20*log10(abs(H(2*pi*f, K, 2*pi*fc)))

# Plotting Configuration
figure(num = 2, figsize = (16, 12), dpi = 100, facecolor='w', edgecolor='k')
plot(f, H_log)
xscale('log')
title(r'Unity-Gain HPF Frequency Response, $f_{3dB}$ = %s Hz' %fc)
xlabel('Frequency [Hz]')
ylabel('Gain [dB]')
grid(True)

savefig('HPF.png')