import sys
import dataclasses
from typing import Sequence
import numpy as np


@dataclasses.dataclass
class Packet:
  version: int
  type_id: int


@dataclasses.dataclass
class Literal(Packet):
  value: int


@dataclasses.dataclass
class Operator(Packet):
  packets: Sequence[Packet]

  @property
  def value(self):
    s = np.array([p.value for p in self.packets])
    return {
        0: np.sum,
        1: np.prod,
        2: np.min,
        3: np.max,
        5: lambda s: s[0] > s[1] and 1 or 0,
        6: lambda s: s[0] < s[1] and 1 or 0,
        7: lambda s: s[0] == s[1] and 1 or 0
    }[self.type_id](s)


bits = bin(int(sys.stdin.readline(), 16))[2:]


def parse(bits):
  version, type_id, bits = bits[:3], bits[3:6], bits[6:]
  version = int(version, 2)
  type_id = int(type_id, 2)

  if type_id == 4:
    value = 0
    while True:
      cont, digit, bits = bits[0], bits[1:5], bits[5:]
      cont, digit = int(cont, 2), int(digit, 2)
      value = value * 16 + digit

      if cont == 0: break
    return Literal(version, type_id, value), bits
  else:
    i, bits = bits[0], bits[1:]
    i = int(i, 2)
    if i == 0:
      subpacket_length, bits = bits[:15], bits[15:]
      subpacket_length = int(subpacket_length, 2)
      sub_bits, bits = bits[:subpacket_length], bits[subpacket_length:]
      subpackets = []
      while sub_bits:
        subpacket, sub_bits = parse(sub_bits)
        subpackets.append(subpacket)
      return Operator(version, type_id, tuple(subpackets)), bits
    else:
      subpacket_count, bits = bits[:11], bits[11:]
      subpacket_count = int(subpacket_count, 2)
      subpackets = []
      for i in range(subpacket_count):
        subpacket, bits = parse(bits)
        subpackets.append(subpacket)
      return Operator(version, type_id, tuple(subpackets)), bits


def sum_versions(packet):
  if packet.type_id == 4:
    return packet.version
  return packet.version + sum(sum_versions(p) for p in packet.packets)


print('version', sum_versions(parse(bits)[0]))
print('value', parse(bits)[0].value)