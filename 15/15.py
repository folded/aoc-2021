import sys
import numpy as np
import heapq
import numba

mtx = np.array([[int(x) for x in line.strip()] for line in sys.stdin]).T


@numba.njit
def solve(mtx, repeats):
  pos = [(0, (0, 0))]
  shape = np.array(mtx.shape) * repeats
  visited = np.zeros((shape[0], shape[1]), dtype=np.bool_)
  visited[0, 0] = True

  while True:
    score, (x, y) = heapq.heappop(pos)
    if x == shape[0] - 1 and y == shape[1] - 1:
      return score
    for x2, y2 in ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)):
      if visited[max(0, min(x2, shape[0] - 1)), max(0, min(y2, shape[1] - 1))]:
        continue
      xd, xm = divmod(x2, mtx.shape[0])
      yd, ym = divmod(y2, mtx.shape[1])
      s = (mtx[xm, ym] + xd + yd - 1) % 9 + 1
      heapq.heappush(pos, (score + s, (x2, y2)))
      visited[x2, y2] = True


TIMING = False

import time
for i in (1, 5):
  print(solve(mtx, i))
  if TIMING:
    t = []
    for times in range(100):
      a = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
      solve(mtx, i)
      b = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
      t.append(b - a)
    print('median time (ms): ', np.median(np.array(t)) / 1e6)
