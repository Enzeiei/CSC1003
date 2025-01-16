#!/usr/bin/env python3

import sys

no = sys.argv[1:]
nums = " ".join(no)

lii = sys.stdin.read().split()

gat = 3
rate = [0, 1, 5, 100]

ii = 0
while ii < len(lii) // gat:
  multi = 0
  point = ii * gat
  bimp = [lii[point], lii[point + 1], lii[point + 2]]
  run = 0
  while run < len(no):
    if no[run] in bimp:
      multi += 1
    run += 1
  print(rate[multi])
  ii += 1
