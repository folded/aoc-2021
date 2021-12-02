import sys

x = y = 0

for line in sys.stdin:
    cmd, val = line.strip().split()
    val = int(val)
    if cmd == 'forward':
        x += val
    elif cmd == 'down':
        y += val
    elif cmd == 'up':
        y = max(0, y - val)

print(x*y)