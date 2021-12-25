import sys
import numpy as np
import itertools

state = np.array([list(x.strip()) for x in sys.stdin])

def can_move(state, axis):
  return np.roll(state, -1, axis=axis) == '.'

def will_move(state, axis):
  return state == 'v>'[axis]

def move(state, axis):
  movers = can_move(state, axis) & will_move(state, axis)
  new_state = np.where(movers, np.array(['.']), state)
  new_state[np.roll(movers, 1, axis)] = 'v>'[axis]
  return movers.sum(), new_state

for i in itertools.count(1):
  ne, state = move(state, 1)
  ns, state = move(state, 0)
  if ne + ns == 0:
    break

print(i)