#!/usr/bin/env python

import time, math
from blinkt import set_brightness, set_pixel, show

try:
    import psutil
except ImportError:
    exit("This library requires the psutil module\nInstall with: sudo pip install psutil") 

def show_graph(v, r, g, b):
    v *= 8
    for x in range(8):
        if v  < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v,1.0) * c) for c in [r,g,b]]
        set_pixel(x, r, g, b)
        v -= 1

    show()

set_brightness(0.1)

while True:
    v = psutil.cpu_percent() / 100.0
    show_graph(v, 255, 255, 255)
    time.sleep(0.01)
