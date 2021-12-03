import sys
import numpy as np

mtx = np.array([ list(map(int, line.strip())) for line in sys.stdin ])
bits = mtx.sum(axis=0) > mtx.shape[0] // 2
gamma = (bits[::-1] * 2 ** np.arange(0, bits.shape[0])).sum()
epsilon = (~bits[::-1] * 2 ** np.arange(0, bits.shape[0])).sum()
print(gamma, epsilon, gamma * epsilon)