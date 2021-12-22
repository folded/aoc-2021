import dataclasses
import sys
import re
import numpy as np
import statistics


@dataclasses.dataclass
class Cube:
  op: str
  lo: np.ndarray
  hi: np.ndarray

  def __repr__(self):
    return f'<{self.op}:{tuple(self.lo)}..{tuple(self.hi)}>'

  def __post_init__(self):
    self.lo = np.array(self.lo, dtype=int)
    self.hi = np.array(self.hi, dtype=int)

  def same(self, other: 'Cube'):
    return np.all(self.lo == other.lo) and np.all(self.hi == other.hi)

  def split(self, axis, pos):
    if self.hi[axis] <= pos:
      return [self, None]
    if pos <= self.lo[axis]:
      return [None, self]
    hi = np.array(self.hi, dtype=int)
    hi[axis] = pos
    lo = np.array(self.lo, dtype=int)
    lo[axis] = pos
    return [Cube(self.op, self.lo, hi), Cube(self.op, lo, self.hi)]

  @property
  def volume(self):
    return np.product(self.hi - self.lo)

  @classmethod
  def make(cls, line):
    m = re.match(
        r'(on|off) '
        r'x=(-?[0-9]+)[.][.](-?[0-9]+),'
        r'y=(-?[0-9]+)[.][.](-?[0-9]+),'
        r'z=(-?[0-9]+)[.][.](-?[0-9]+)', line).groups()
    return Cube(m[0], np.array((int(m[1]), int(m[3]), int(m[5])), dtype=int),
                np.array((int(m[2]), int(m[4]), int(m[6])), dtype=int) + 1)


cubes = [Cube.make(l) for l in sys.stdin]


def subdivide(cubes, depth=0):
  if not len(cubes):
    return 0

  if all(cubes[0].same(c) for c in cubes[1:]):
    return cubes[-1].volume if cubes[-1].op == 'on' else 0

  axis = depth % 3
  p = set()
  for c in cubes:
    p.update([c.lo[axis], c.hi[axis]])
  mid = statistics.median_low(sorted(p))

  l, r = zip(*[c.split(axis, mid) for c in cubes])

  return (subdivide([x for x in l if x], depth + 1) +
          subdivide([x for x in r if x], depth + 1))


init = np.zeros((101, 101, 101), dtype=bool)
for c in cubes:
  lo = np.minimum(np.maximum(c.lo + 50, 0), 101)
  hi = np.minimum(np.maximum(c.hi + 50, 0), 101)
  init[lo[0]:hi[0], lo[1]:hi[1], lo[2]:hi[2]] = c.op == 'on'

print(init.sum())

print(subdivide(cubes))
