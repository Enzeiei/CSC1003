#!/usr/bin/env python3

import sys

args = sys.argv[1:]
zeta = int(args[0])

em = 1
while em <= zeta:
  print((" " * ((zeta - em) // 2)) + (em * "*"))
  em += 2

em -= 4
while not em < 1:
  print((" " * ((zeta - em) // 2)) + em * "*")
  em -= 2
