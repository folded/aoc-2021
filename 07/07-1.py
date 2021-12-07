import sys
import statistics
import numpy as np

pos = np.array([int(x) for x in sys.stdin.readline().split(',')])
median = statistics.median_low(pos)
print(np.sum(np.abs(median - pos)))
