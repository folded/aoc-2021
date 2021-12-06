import sys
import numpy as np
import collections

state = np.bincount([int(x) for x in sys.stdin.readline().split(',')],minlength=9)
 
print(state)

for i in range(256):
  zeros = state[0]
  state[7] += zeros
  state[:-1] = state[1:]
  state[8]=zeros

print(state.sum())

