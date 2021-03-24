import math

mW = 4095875
W = mW/1000


if math.isclose(W, 4095.88, abs_tol=0.1):
    print("Equal with tolerance of 0.1")