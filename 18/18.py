import copy
import itertools
import sys


class Repeat(Exception):
  pass


def add_xmost(path, child, val, L, R):
  while path and child is path[-1][L]:
    path, child = path[:-1], path[-1]
  if not path:
    return
  node = path[-1]
  if not isinstance(node[L], list):
    node[L] = node[L] + val
    return
  node = node[L]
  while isinstance(node[R], list):
    node = node[R]
  node[R] = node[R] + val


def explode(a, depth, path):
  x, y = a

  if isinstance(x, list):
    if depth == 3:
      add_xmost(path + (a, ), x, x[0], 0, 1)
      add_xmost(path + (a, ), x, x[1], 1, 0)
      a[0] = 0
      raise Repeat()
    else:
      explode(x, depth + 1, path + (a, ))

  if isinstance(y, list):
    if depth == 3:
      add_xmost(path + (a, ), y, y[0], 0, 1)
      add_xmost(path + (a, ), y, y[1], 1, 0)
      a[1] = 0
      raise Repeat()
    else:
      explode(y, depth + 1, path + (a, ))


def split(a):
  x, y = a

  if isinstance(x, list):
    split(x)
  elif x >= 10:
    a[0] = [x // 2, x - x // 2]
    raise Repeat()

  if isinstance(y, list):
    split(y)
  elif y >= 10:
    a[1] = [y // 2, y - y // 2]
    raise Repeat()


def simplify(a):
  a = copy.deepcopy(a)
  while True:
    try:
      explode(a, 0, ())
      split(a)
      return a
    except Repeat:
      continue


def magnitude(a):
  if not isinstance(a, list):
    return a
  return (3 * magnitude(a[0]) + 2 * magnitude(a[1]))


def add(a, b):
  return simplify([a, b])


numbers = [eval(line) for line in sys.stdin]

a = numbers[0]
for b in numbers[1:]:
  a = add(a, b)
print(magnitude(a))

print(
    max(
        magnitude(add(a, b))
        for a, b in itertools.product(numbers, numbers)
        if a is not b
    ))
