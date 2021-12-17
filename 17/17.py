# input: target area: x=102..157, y=-146..-90
# sample: target area: x=20..30, y=-10..-5    -> initial velocity = 6,9 max y = 45
#   max y = dy*(dy+1)/2

import numba
import numpy as np


@numba.njit
def simulate(dx, dy):
  # target = ((20, 30), (-10, -5))
  target = ((102, 157), (-146, -90))
  x = 0
  y = 0
  while y >= target[1][0]:
    x += dx
    y += dy
    ddy = 1
    if dx: dx -= dx // abs(dx)
    dy -= 1
    if target[0][0] <= x <= target[0][1] and target[1][0] <= y <= target[1][1]:
      return True, (x, y)
  return False, (x, y)


max_dy = -147
solutions = set()
for dy in range(-147, 147):
  dx_list = []
  for dx in range(0, 158):
    hit, (x, y) = simulate(dx, dy)
    if hit:
      solutions.add((dx, dy))
      max_dy = dy

solutions = np.array(sorted(solutions))

print(max_dy * (max_dy + 1) // 2)
print(solutions.shape[0])