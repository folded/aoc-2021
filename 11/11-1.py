import sys
import numpy as np

mtx = np.array([[int(x) for x in line.strip()] for line in sys.stdin])


def flash(mtx):
  count = 0
  while True:
    mask = mtx >= 10
    c = mask.sum()
    if not c: break
    mtx += np.add.reduce(np.lib.stride_tricks.sliding_window_view(
        np.pad(mask, (1, 1), mode='constant', constant_values=0), [3, 3]),
                         axis=(-2, -1))
    mtx[mask] = -1000
    count += c
  mtx[mtx < 0] = 0
  return count


count = 0
for i in range(100):
  mtx += 1
  count += flash(mtx)

print(count)