#!/usr/bin/env python3

import sys

gripp = (sys.argv[1:])[0]
lgrip = len(gripp)
chance = []
inzie = input()
mayo = []

while inzie != "end":
  mayo.append(inzie)
  inzie = input()

zz = 0
while zz < len(mayo):
  exo = 0
  while exo + lgrip <= len(mayo[zz]):
    if (mayo[zz])[exo:exo + lgrip] == gripp:
      chance.append(zz)
      exo = len(mayo[zz])
    exo += 1
  zz += 1

ee = 0
while ee < len(chance):
  print(mayo[chance[ee]])
  ee += 1
