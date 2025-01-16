#!/usr/bin/env python3

import sys

fac = sys.argv[1:]

f = 0
while f < len(fac):
  fac[f] = int(fac[f])
  f += 1
# print(fac)

rei = sys.stdin.read().split()
# rei = "10\n12\n4\n7\n24\n120\n121\n".split()

# print(rei)
r = 0
while r < len(rei):
  rei[r] = int(rei[r])
  r += 1
# print(rei)

c = 0
while c < len(rei):
  d = 0
  while d < len(fac) and (rei[c] % fac[d] == 0):
    d += 1
  if not d < len(fac):
    print(rei[c])
  c += 1
