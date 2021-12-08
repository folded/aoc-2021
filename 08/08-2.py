import sys
import itertools

canonical = {
    1: frozenset('cf'),
    7: frozenset('acf'),
    4: frozenset('bcdf'),
    2: frozenset('acdeg'),
    3: frozenset('acdfg'),
    5: frozenset('abdfg'),
    0: frozenset('abcefg'),
    6: frozenset('abdefg'),
    9: frozenset('abcdfg'),
    8: frozenset('abcdefg'),
}
canonical_inv = {v: k for k, v in canonical.items()}
all_digits = frozenset(canonical.values())


def parse_row(line):
  segments, display = [x.strip().split() for x in line.split('|')]
  assert len(segments) == 10
  assert len(display) == 4
  return segments, display


def is_consistent(segments, mapping):
  return all(
      frozenset(mapping[s] for s in segment) in all_digits
      for segment in segments)


def make_mapping(segments):
  for perm in itertools.permutations('abcdefg', 7):
    mapping = dict(zip(perm, 'abcdefg'))
    if is_consistent(segments, mapping):
      return mapping


inputs = [parse_row(line) for line in sys.stdin]

tot = 0
for segments, display in inputs:
  mapping = make_mapping(segments)
  s = sum([
      10**i * canonical_inv[frozenset(mapping[c] for c in d)]
      for i, d in zip((3, 2, 1, 0), display)
  ])
  tot += s

print(tot)