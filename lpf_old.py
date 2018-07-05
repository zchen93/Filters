
import numpy as np
from numpy import sqrt
import matplotlib.pyplot as plt
import scipy as sp 
import math
from scipy import signal

W_h = 6000
N = 5000
j = complex(0,1)
pi = np.pi
K = 1 # DC Gain

num_coeff = [K*W_h, 0]
den_coeff = [W_h, 1]

#N = 512  # number of frequency points
Upper_Limit = int(10e3)
dw = Upper_Limit/N # distance between two frequency points

H = np.zeros(N)
for n in range(N):
    w0 = n*dw
    s = j*2*pi*w0

    num = num_coeff[0]
    denom = den_coeff[0] + s
    H[n]=abs(num/denom)

# Now just do the plotting
w = np.arange(0,Upper_Limit,dw)
#plt.plot(w, 20*np.log10(H))
plt.plot(w,H)
plt.ylim((-30,10))
plt.grid(True)

#https://dsp.stackexchange.com/questions/37595/plotting-the-magnitude-response-of-a-filter