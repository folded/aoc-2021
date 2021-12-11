import sys
import statistics

c_score = {
    '(': 1, '[': 2, '{': 3, '<': 4
}
pairs = {'(':')', '[':']', '{': '}', '<':'>'}

def parse(line):
    stack = []
    for c in line:
        if c in pairs:
            stack.append(c)
        elif not len(stack):
            return 0
        elif c != pairs[stack[-1]]:
            return 0
        else:
            stack.pop()
    s = 0
    for c in stack[::-1]:
        s = s * 5 + c_score[c]
    return s

scores = []
for line in sys.stdin:
    score = parse(line.strip())
    if score:
        scores.append(score)
print(statistics.median_low(scores))
