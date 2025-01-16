#!/usr/bin/env python3

import sys

va = int(sys.argv[1:][0])

sad = []
vv = va
sad.append(vv)
e = 0
while e < 9:
  if vv % 2 == 0:
    vv //= 2
  else:
    vv = (vv * 3) + 1
  sad.append(vv)
  e += 1

e = len(sad) - 1
while e >= 0:
  print(sad[e])
  e -= 1
