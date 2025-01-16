#!/usr/bin/env python3

import sys

ll = sys.stdin.read().split()

gat = 3
ii = 0
while ii < len(ll) // gat:
  if int(ll[(ii * gat) + 2]) >= 40:
    print(ll[ii * gat] + " " + ll[(ii * gat) + 1])
  ii += 1
