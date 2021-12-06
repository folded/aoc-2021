import collections
import re
import sys
import numpy as np

line_re = re.compile(r'^(\d+),(\d+) -> (\d+),(\d+)$')

line_list = []
for line in sys.stdin:
    m = line_re.match(line)
    a,b,c,d = [int(x) for x in m.groups()]
    line_list.append(((a,b), (c,d)))


coords = collections.Counter()

for (x1,y1), (x2,y2) in line_list:
    x,y = x1,y1
    dx = (x2-x1)
    dy = (y2-y1)
    if dx: dx=dx//abs(dx)
    if dy: dy=dy//abs(dy)

    while True:
        coords[(x,y)] += 1
        if (x,y) == (x2,y2):
            break
        x,y = x+dx,y+dy

print(len([x for x in coords.values() if x > 1]))
