#!/usr/bin/env python3

import sys

def line():
  print(" --------------------")


coo = sys.stdin.readlines()

ord = {}

tempy = []
aa = []
oo = 0
while oo < len(coo):
  aa = coo[oo].strip().split()
  if aa[1] not in ord:
    ord[aa[1]] = [aa[0]]
  elif aa[1] in ord:
    tempy = ord[aa[1]]
    tempy.append(aa[0])
    ord[aa[1]] = tempy
  oo += 1
# dictionary format is y: [x, x, x]

ok = list(ord.keys())
line()
y = 19
while y >= 0:
  st = "|                    |"
  wy = str(y)
  if wy in ok:
    x = 19
    while x >= 0:
      if str(x) in ord[wy]:
        st = st[:x + 1] + "*" + st[x + 2:]
      x -= 1
  print(st)
  y -= 1
line()
