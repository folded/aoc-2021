import sys
import numpy as np

mtx = np.array([[int(x) for x in line.strip()] for line in sys.stdin])


def fill(mtx, i, j):
  if i < 0 or j < 0 or i >= mtx.shape[0] or j >= mtx.shape[1]:
    return 0
  if mtx[i, j] == 9:
    return 0
  mtx[i, j] = 9
  return (1 +
      fill(mtx, i - 1, j) + fill(mtx, i + 1, j) +
      fill(mtx, i, j - 1) + fill(mtx, i, j + 1))

sizes = []
for i in range(mtx.shape[0]):
  for j in range(mtx.shape[1]):
    sizes.append(fill(mtx, i, j))

sizes.sort()
print(sizes[-3] * sizes[-2] * sizes[-1])
