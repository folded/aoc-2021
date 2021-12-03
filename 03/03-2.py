import sys
import numpy as np

def to_dec(bits):
    return (bits[::-1] * 2 ** np.arange(0, bits.shape[0])).sum()

def find_val(mtx, hi, idx=0):
    if mtx.shape[0] == 1:
        return to_dec(mtx[0])
    assert idx < mtx.shape[1]
    cnt = mtx[:,idx].sum()
    sel = hi ^ (cnt.sum() < mtx.shape[0] / 2)
    return find_val(mtx[mtx[:,idx] != sel], hi, idx + 1)

mtx = np.array([ list(map(int, line.strip())) for line in sys.stdin ])
print(find_val(mtx, 1) * find_val(mtx, 0))