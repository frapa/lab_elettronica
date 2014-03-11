# -*- encoding: utf-8 -*-

import numpy as np

R = np.array((19943, 997, 499550))
C = np.array((99.3e-9, 990e-9, 5e-9))

T = R * C
print(T)

C_inc = 3.04e-3 / 3e3
print(C_inc)
