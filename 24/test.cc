#include <iostream>
#include <stdint.h>

int calculate(int64_t i[14]) {
  int64_t x = 0;
  int64_t y = 0;
  int64_t z = 0;
  int64_t w = 0; 
  int c = 0;

#include "converted.txt"

  return z;
}

int calculate2(int64_t i[14]) {
  int64_t x = 0;
  int64_t y = 0;
  int64_t z = 0;
  int64_t w = 0; 
  int c = 0;

  w = i[0];
  z = w + 14;

  w = i[1];
  z += (25 * z + (w + 2));

  w = i[2];
  z += (25 * z + (w + 1));

  w = i[3];
  z += (25 * z + (w + 13));

  w = i[4];
  z += (25 * z + (w + 5));

  x = z % 26;
  z = z / 26;
  i[5] = x + -12;

  x = z % 26;
  z = z / 26;
  i[6] = x + -12;

  w = i[7];
  z += (25 * z + (w + 9));

  x = z % 26;
  z = z / 26;
  i[8] = x + -7;

  w = i[9];
  z += (25 * z + (w + 13));

  x = z % 26;
  z = z / 26;
  i[10] = x + -8;

  x = z % 26;
  z = z / 26;
  i[11] = x + -5;

  x = z % 26;
  z = z / 26;
  i[12] = x + -10;

  x = z % 26;
  z = z / 26;
  i[13] = x + -7;

  return z;
}

int main(int argc, char **argv) {
  int64_t i[14];
  int unknowns[7] = {9,7,4,3,2,1,0};

  std::fill(i, i+14, 9);
  bool done = false;

  while (!done) {
    calculate2(i);
    // for (int j = 0; j < 14; ++j) std::cout << i[j] << " ";
    // std::cout << std::endl;
    assert(calculate(i) == 0);
    if (std::all_of(i, i+14, [](int a) { return a > 0 && a < 10; })) {
      for (int j = 0; j < 14; ++j) std::cout << i[j];
      std::cout << std::endl;
    }
    done = true;
    for (int j : unknowns) {
      if (--i[j] > 0) { done = false; break; }
      i[j] = 9;
    }
  }
}