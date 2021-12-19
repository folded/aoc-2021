import collections
import dataclasses
import io
import re
import sys
import itertools
import numpy as np
from typing import Optional, Sequence, Tuple


@dataclasses.dataclass(frozen=True, order=True)
class Registration:
  orientation: int
  offset: Tuple[int, int, int]


def _rot(o: int):
  x = np.roll(np.array([1, 0, 0]), o % 3)
  o //= 3
  x *= 1 - 2 * (o & 1)
  o //= 2
  y = np.roll(x, 1 + (o & 1))
  o //= 2
  y *= 1 - 2 * (o & 1)
  z = np.cross(x, y)
  return np.array((x, y, z))


ROT = [_rot(i) for i in range(24)]


class Scanner:
  def __init__(self, identifier: int, beacons: Sequence[Tuple[int, int, int]]):
    self._identifier = identifier
    self._beacons = np.array(beacons)
    self._registration = None

  @property
  def position(self) -> np.ndarray:
    assert self.is_registered
    return np.array(self._registration.offset)

  @property
  def is_registered(self) -> bool:
    return self._registration is not None

  def set_registration(self, registration: Registration):
    assert not self.is_registered
    self._registration = registration
    self._beacons = self.get_beacons(registration.orientation) - np.array(
        registration.offset)

  @property
  def registered_beacons(self):
    assert self.is_registered
    return [tuple(b) for b in self._beacons]

  def get_beacons(self, orientation: int):
    return self._beacons @ ROT[orientation]

  def _best_registration_for(self, other: 'Scanner',
                             orientation: int) -> Tuple[int, Registration]:
    a = self.get_beacons(0)
    b = other.get_beacons(orientation)
    offset_counts = collections.Counter()
    for i in range(a.shape[0]):
      for j in range(b.shape[0]):
        offset_counts[tuple(b[j] - a[i])] += 1
    offset, matches = offset_counts.most_common(1)[0]
    return matches, Registration(orientation, offset)

  def best_registration_for(self,
                            other: 'Scanner') -> Tuple[int, Registration]:
    return max(self._best_registration_for(other, o) for o in range(24))

  @classmethod
  def read(cls, input: io.FileIO) -> Optional['Scanner']:
    while True:
      line = input.readline()
      if line == '':
        return None
      if line.strip() != '':
        break
    m = re.match(r'--- scanner (\d+) ---', line)
    idenifier = int(m.group(1))
    beacons = []
    for line in input:
      if line.strip() == '':
        break
      beacons.append(tuple(int(c) for c in line.split(',')))
    return cls(idenifier, beacons)


scanners = []
while True:
  s = Scanner.read(sys.stdin)
  if s is None:
    break
  scanners.append(s)

scanners[0].set_registration(Registration(0, (0, 0, 0)))

while not all(s.is_registered for s in scanners):
  registered = [s for s in scanners if s.is_registered]
  unregistered = [s for s in scanners if not s.is_registered]
  for u in unregistered:
    for r in registered:
      n, reg = r.best_registration_for(u)
      if n >= 12:
        u.set_registration(reg)
        break
    else:
      continue
    break

beacons = set()
for s in scanners:
  beacons.update(s.registered_beacons)

print(len(beacons))

print(
    max(
        np.abs(s1.position - s2.position).sum()
        for s1, s2 in itertools.product(scanners, scanners)))
