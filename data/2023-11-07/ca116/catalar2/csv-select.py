#!/usr/bin/env python3

import sys

# The first command-line argument is at position 1...
#
pos = (sys.argv[1])
run = 0
while pos[run] != "=":
  run += 1
compa = pos[:run]
tyr = pos[run + 1:]


zssa = input()
epi = []
ee = 0
while zssa != "end":
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
  if epi[0][em] == compa:
    preserv = em
  em += 1
rr = 1
while rr < len(epi):
  if epi[rr][preserv] == tyr:
    m = 0
    temper = ""
    while m < len(epi[rr]):
      temper += str(epi[rr][m]) + ","
      m += 1
    print(temper[:(len(temper) - 1)])
  rr += 1
