import sys

canonical = {
  1: 'cf',
  7: 'acf',
  4: 'bcdf',
  2: 'acdeg',
  3: 'acdfg',
  5: 'abdfg',
  0: 'abcefg',
  6: 'abdefg',
  9: 'abcdfg',
  8: 'abcdefg',
}
lengths = {}
for c in canonical:
  lengths.setdefault(len(canonical[c]), []).append(c)

def parse_row(line):
  segments, display = [x.strip().split() for x in line.split('|')]
  assert len(segments) == 10
  assert len(display) == 4
  return segments, display

part1 = 0

for line in sys.stdin:
  segments, display = parse_row(line)
  for d in display:
    if len(lengths[len(d)]) == 1:
      c = lengths[len(d)][0]
    else:
      c = None
    if c is not None:
      part1 += 1

print(part1)