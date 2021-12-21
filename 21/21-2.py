import sys
import re
import itertools
import collections
import functools
import numba

positions = [
    int(re.match(r'Player (\d) starting position: (\d+)$', line).group(2))
    for line in sys.stdin
]
scores = [0] * len(positions)

moves = tuple(
    collections.Counter([
        a + b + c
        for a, b, c in itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3))
    ]).items())


@numba.njit
def play(positions, scores):
  def moved(p, n):
    return ((p + n - 1) % 10) + 1

  if scores[1] >= 21:
    return (0, 1)

  t = (0, 0)
  for m, n in moves:
    p = (positions[1], moved(positions[0], m))
    s = (scores[1], scores[0] + p[1])
    r = play(p, s)
    t = t[0] + r[1] * n, t[1] + r[0] * n
  return t


print(play(tuple(positions), tuple(scores)))
