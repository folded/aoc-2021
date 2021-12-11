import sys
import numpy as np

mtx = np.array([[int(x) for x in line.strip()] for line in sys.stdin])

def flash(mtx):
    count = 0
    while True:
        c = 0
        for i in range(mtx.shape[0]):
            for j in range(mtx.shape[1]):
                il, jl = max(i-1,0), max(j-1,0)
                ih, jh = min(i+2, mtx.shape[0]), min(j+2, mtx.shape[1])
                if mtx[i,j] >= 10:
                    mtx[il:ih, jl:jh] += 1
                    mtx[i,j] = -100
                    c += 1
        count += c
        if not c:
            break
    return count

count = 0
for i in range(100):
    mtx += 1
    count += flash(mtx)
    mtx[mtx<0] = 0
    print(mtx)

print(count)