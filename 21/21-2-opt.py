import sys
import re
import itertools
import collections
import numba
import numpy as np

positions = [
    int(re.match(r'Player (\d) starting position: (\d+)$', line).group(2))
    for line in sys.stdin
]
scores = [0] * len(positions)

moves = np.array(tuple(
    collections.Counter([
        a + b + c
        for a, b, c in itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3))
    ]).items()),
                 dtype=np.int64)

@numba.njit
def play(positions, scores, cache):
  if scores[1] >= 21:
    return np.array([0, 1], dtype=np.int64)

  key = positions[0] * 1_00_00_00 + positions[1] * 1_00_00 + scores[
      0] * 1_00 + scores[1]
  if key in cache:
    return cache[key]

  def moved(p, n):
    return ((p + n - 1) % 10) + 1

  t = np.zeros(2, dtype=np.int64)
  for m, n in moves:
    p = (positions[1], moved(positions[0], m))
    s = (scores[1], scores[0] + p[1])
    r = play(p, s, cache)
    t[0] += r[1] * n
    t[1] += r[0] * n

  cache[key] = t
  return t


int_array = numba.types.int64[:]
import time

print(
    play(
        tuple(positions), tuple(scores),
        numba.typed.Dict.empty(key_type=numba.types.int64,
                               value_type=int_array)))
a = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
print(
    play(
        tuple(positions), tuple(scores),
        numba.typed.Dict.empty(key_type=numba.types.int64,
                               value_type=int_array)))
b = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
print((b - a) / 1e9)