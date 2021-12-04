import sys
import numpy as np


def read_boards(f):
  while True:
    board = []
    while len(board) < 5:
      line = f.readline()
      if line == '':
        return
      row = [int(x) for x in line.strip().split()]
      if len(row):
        assert len(row) == 5
        board.append(row)
    yield np.array(board)


order = [int(x) for x in sys.stdin.readline().split(',')]

boards = list(read_boards(sys.stdin))

for o in order:
  for b in boards:
    b[b == o] = -1
    if np.any(b.sum(0) == -5) or np.any(b.sum(1) == -5):
      print(np.maximum(0, b).sum() * o)
      sys.exit(0)
