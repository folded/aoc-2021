import sys
import numpy as np
import heapq
import itertools

mtx = np.array([[int(x) for x in line.strip()] for line in sys.stdin]).T


def solve(mtx, repeats):
  pos = [(0, (0, 0))]
  visited = {(0, 0)}

  def neighbours(x, y, visited):
    if x > 0 and (x - 1, y) not in visited: yield (x - 1, y)
    if y > 0 and (x, y - 1) not in visited: yield (x, y - 1)
    if x < mtx.shape[0] * repeats - 1 and (x + 1, y) not in visited:
      yield (x + 1, y)
    if y < mtx.shape[1] * repeats - 1 and (x, y + 1) not in visited:
      yield (x, y + 1)

  while True:
    score, (x, y) = heapq.heappop(pos)
    if x == mtx.shape[0] * repeats - 1 and y == mtx.shape[1] * repeats - 1:
      return score
    for x2, y2 in neighbours(x, y, visited):
      xd, xm = divmod(x2, mtx.shape[0])
      yd, ym = divmod(y2, mtx.shape[1])
      s = (mtx[xm, ym] + xd + yd - 1) % 9 + 1
      heapq.heappush(pos, (score + s, (x2, y2)))
      visited.add((x2, y2))


print(solve(mtx, 1))
print(solve(mtx, 5))