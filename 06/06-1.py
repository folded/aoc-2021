import sys
import numpy as np

state = np.array([int(x) for x in sys.stdin.readline().split(',')])

for i in range(80):
  zeros = state.shape[0] - np.count_nonzero(state)
  state[state == 0] = 7
  state = np.concatenate([state, np.full((zeros,), 9)])
  state -= 1

print(state.shape[0])