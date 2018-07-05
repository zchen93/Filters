# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 22:02:29 2018

@author: Zengweijie (Fred) Chen

Frequency Response Plot
Band-Pass Filter

""" 

from pylab import *

f_l = 400
f_h = 120000

K = 1
f = logspace(1,7) # frequencies from 10^1 to 10^5

def FreqResp(w, K, wl, wh):
    H_LPF = 1 / (1.0 + 1j * w / wh)
    H_HPF = K*1j*w / (wl + 1j*w)
    H = H_LPF * H_HPF
    return H

H_log = 20*log10(abs(FreqResp(2*pi*f, K, 2*pi*f_l, 2*pi*f_h)))


# Plotting Configuration
figure(num = 1, figsize = (16, 12), dpi = 100, facecolor='w', edgecolor='k')
plot(f, H_log)
xscale('log')
title(r'Unity-Gain BPF Frequency Response, %s Hz & %s Hz' %(f_l, f_h))
xlabel('Frequency [Hz]')
ylabel('Gain [dB]')
grid(True)

savefig('BPF.png')