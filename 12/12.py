import sys
import re
import collections

graph = collections.defaultdict(set)
for row in sys.stdin:
    a,b = row.strip().split('-')
    graph[a].add(b)
    graph[b].add(a)

def n_paths(graph, node, little, dup_little):
    if node == 'end':
        return 1
    count = 0
    for dest in graph[node]:
        if dest == 'start':
            continue
        if re.match(r'^[A-Z]+$', dest):
            count += n_paths(graph, dest, little, dup_little)
        elif dest in little and not dup_little:
            count += n_paths(graph, dest, little, True)
        elif dest not in little:
            count += n_paths(graph, dest, set.union({dest}, little), dup_little)
    return count

print('part 1', n_paths(graph, 'start', set(), True))
print('part 2', n_paths(graph, 'start', set(), False))
