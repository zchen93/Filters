# Filter Simulation
# 1. LPF and Active LPF
# 2. HPF and Active HPF
# 3. BPF and Active BPF
# Fred Chen, 20180623
import numpy as np
import os
import lpf
# print os.system("clear"), chr(13), " ", chr(13),

def main():
    # Up and running
    type = input('What type of filter do you want to see? ')
    if type == 'LPF' or 'Low Pass Filter' or "Low-Pass Filter" or 'Low Pass' or "Low-Pass" or 'LP':
        gain = input('How much gain do you want? ')
        if gain > 0:
            #xxxxxx
            if gain >= 1:
                #eeeeee
                return 0
            return 1
