#!/usr/bin/env python3

import sys

# print(sys.argv[0])

args = sys.argv[1:]

zeta = len(args)

zz = 0
while zz < zeta:
  print(args[zz])
  zz += 1
