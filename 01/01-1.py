import sys

import numpy as np

arr = np.array(list(map(int, sys.stdin.readlines())))
print(((arr[1:]  - arr[:-1])>0).sum())