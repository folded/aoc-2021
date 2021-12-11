import sys

c_score = {
    ')': 3, ']': 57, '}': 1197, '>': 25137
}
pairs = {'(':')', '[':']', '{': '}', '<':'>'}

def parse(line):
    stack = []
    for c in line:
        if c in pairs:
            stack.append(c)
        elif not len(stack):
            return 0  # incomplete
        elif c != pairs[stack[-1]]:
            return c_score[c]
        else:
            stack.pop()
    return 0

score = 0
for line in sys.stdin:
    score += parse(line.strip())
print(score)