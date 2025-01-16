#!/usr/bin/env python3

import sys

# print(sys.argv[0])

args = sys.argv[1:]

zeta = len(args)
totalus = 0

zz = 0
while zz < zeta:
  totalus += int(args[zz])
  zz += 1

print(totalus)
