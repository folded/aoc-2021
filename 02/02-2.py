import sys

x = y = aim = 0

for line in sys.stdin:
    cmd, val = line.strip().split()
    val = int(val)
    if cmd == 'forward':
        x += val
        y += val * aim
    elif cmd == 'down':
        aim += val
    elif cmd == 'up':
        aim -= val

print(x*y)