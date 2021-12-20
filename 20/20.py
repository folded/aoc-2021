import sys
import numpy as np

p = (2**np.arange(9))[::-1]


def apply_lut(lut, img):
  v = np.lib.stride_tricks.sliding_window_view(np.pad(img, [2, 2]), [3, 3])
  return lut[(np.reshape(v, (v.shape[0], v.shape[1], -1)) * p).sum(axis=2)]


lut = np.array([x == '#' for x in sys.stdin.readline().strip()], dtype=int)
sys.stdin.readline()
img = np.array([[x == '#' for x in line.strip()] for line in sys.stdin],
               dtype=int)

img = np.pad(img, [100, 100])
for i in range(50):
  img = apply_lut(lut, img)
  if i in (1, 49):
    print(img[100:-100, 100:-100].sum())
