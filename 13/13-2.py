import sys
import re
import numpy as np

def _fold(coord, axis, val):
  coord = list(coord)
  if coord[axis] > val:
    coord[axis] = 2 * val - coord[axis]
  return tuple(coord)


def fold(coords, axis, val):
  return {_fold(coord, axis, val) for coord in coords}


coords = set()
while True:
  line = sys.stdin.readline()
  if line.strip() == '':
    break
  x, y = line.strip().split(',')
  coords.add((int(x), int(y)))

while True:
  line = sys.stdin.readline()
  if line.strip() == '':
    break
  m = re.match(r'fold along ([xy])=([0-9]+)', line)
  if m is not None:
    axis, val = m.groups()
    axis = ord(axis) - ord('x')
    val = int(val)
    coords = fold(coords, axis, val)

coords = np.array(list(coords))
mtx = np.zeros(np.max(coords, axis = 0)+1, dtype=int)
for c in coords:
  mtx[c[0], c[1]] = 1
for row in mtx.T:
  line = ''.join([ ' #'[x] for x in row ])
  print(line)