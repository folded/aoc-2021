import sys
import re
import functools

template = sys.stdin.readline().strip()
insertions = {}


def add_counts(a, b, adj):
  return {
      i: a.get(i, 0) + b.get(i, 0) - adj.get(i, 0)
      for i in set.union(set(a.keys()), set(b.keys()))
  }


@functools.lru_cache(None)
def count(pair, depth):
  if depth == 0:
    return add_counts({pair[0]: 1}, {pair[1]: 1}, {})
  return add_counts(count((pair[0], insertions[pair]), depth - 1),
                    count((insertions[pair], pair[1]), depth - 1),
                    {insertions[pair]: 1})


def solve(depth):
  tot = {}
  adj = {}

  for pair in zip(template[:-1], template[1:]):
    tot = add_counts(tot, count(pair, depth), adj)
    adj = {pair[1]: 1}

  tot = sorted(tot.values())
  return tot[-1] - tot[0]


for line in sys.stdin:
  m = re.match(r'(..) -> (.)', line)
  if m is not None:
    insertions[tuple(m.group(1))] = m.group(2)


print(solve(10))
print(solve(40))