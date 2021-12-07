import sys
import statistics
import numpy as np

pos = np.array([int(x) for x in sys.stdin.readline().split(',')])

tot = [
    np.sum(np.abs(i - pos) * (np.abs(i - pos) + 1) / 2)
    for i in range(np.min(pos), np.max(pos))
]

print(np.min(tot))
