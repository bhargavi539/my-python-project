import math

try:
    print(math.exp(1000))
except Exception as e:
    print("Overflow error,Please try a lower exponential value:",e)