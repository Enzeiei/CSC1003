#!/usr/bin/env python3

import sys

# The first command-line argument is at position 1...
#
pos = (sys.argv[1])
zssa = input()
epi = []
ee = 0
while ee < 2:
  point = 0
  teal = []
  find = 0
  while find < len(zssa):
    if zssa[find] == ",":
      teal.append(zssa[point:find])
      point = find + 1
    find += 1
  teal.append(zssa[point:find])
  epi.append(teal)
  zssa = input()
  ee += 1

preserv = 0
em = 0
while em < len(epi[0]):
  if epi[0][em] == pos:
    preserv = em
  em += 1
print(preserv)
