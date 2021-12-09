import sys
import numpy as np

mtx = np.array([[int(x) for x in line.strip()] for line in sys.stdin])
mtx = np.pad(mtx, 1, mode='constant', constant_values=10)

tot = 0

for pos in np.lib.stride_tricks.sliding_window_view(mtx, [3, 3]).reshape(
    (-1, 3, 3)):
  if pos[1, 1] < min(pos[0, 1], pos[1, 0], pos[2, 1], pos[1, 2]):
    tot += pos[1, 1] + 1

print(tot)