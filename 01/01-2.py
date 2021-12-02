import sys

import numpy as np
import numpy.lib.stride_tricks as stride

arr = np.array(list(map(int, sys.stdin.readlines())))
arr = stride.sliding_window_view(arr, 3).sum(axis=1)
print(((arr[1:]  - arr[:-1])>0).sum())