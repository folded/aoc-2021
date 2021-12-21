import sys
import re
import itertools

positions = [
    int(re.match(r'Player (\d) starting position: (\d+)$', line).group(2))
    for line in sys.stdin
]
scores = [0] * len(positions)


def roll():
  n = 0
  while True:
    for i in range(1, 101):
      yield (i, n)
      n += 1


die = roll()

turn = 0
while all(s < 1000 for s in scores):
  positions[turn] += (next(die)[0] + next(die)[0] + next(die)[0])
  positions[turn] = ((positions[turn] - 1) % 10) + 1
  scores[turn] += positions[turn]
  turn = (turn + 1) % len(positions)

print(next(die)[1] * max(s for s in scores if s < 1000))
