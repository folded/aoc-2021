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


def has_won(board):
  return np.any(board.sum(0) == -5) or np.any(board.sum(1) == -5)


def board_score(board):
  return np.maximum(0, board).sum()


def run(boards, order):
  winners = set()
  for io, o in enumerate(order):
    for ib, b in enumerate(boards):
      if ib in winners:
        continue
      b[b == o] = -1
      if has_won(b):
        winners.add(ib)
        yield ib, board_score(b) * o


order = [int(x) for x in sys.stdin.readline().split(',')]

boards = list(read_boards(sys.stdin))

for win in run(boards, order):
  print(win)