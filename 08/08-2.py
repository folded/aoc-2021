import sys

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

canonical_inv = { v: k for k,v in canonical.items() }

ALL = frozenset('abcdefg')

def parse_row(line):
  segments, display = [x.strip().split() for x in line.split('|')]
  assert len(segments) == 10
  assert len(display) == 4
  return segments, display

def is_digit_consistent(digit, value):
  if len(digit) != len(canonical[value]):
    return False
  determined = set(d for d in digit if d.islower())
  return determined.issubset(canonical[value])

def is_consistent(segments, mapping):
  for segment in segments:
    mapped = ''.join(mapping.get(s, s.upper()) for s in segment)
    if not any(is_digit_consistent(mapped, i) for i in range(10)):
      return False
  return True

def _make_mapping(segments, mapping):
  if len(mapping) == 7:
    yield mapping
  else:
    for f in ALL - set(mapping.keys()):
      for t in ALL - set(mapping.values()):
        temp = {**mapping, **{f:t}}
        if is_consistent(segments, temp):
          yield from _make_mapping(segments, temp)

def make_mapping(segments):
  return next(_make_mapping(segments, {}))

inputs = [ parse_row(line) for line in sys.stdin]

tot = 0
for segments, display in inputs:
  mapping = make_mapping(segments)
  s =sum([10**i * canonical_inv[frozenset(mapping[c] for c in d)] for i,d in zip((3,2,1,0),display)])
  tot += s

print(tot)