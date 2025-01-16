#!/usr/bin/env python3

import sys

na = sys.argv[1]
# print(na)
with open(na, "r") as f:
  n2 = f.read()

with open(n2, "r") as g:
  print(g.read().rstrip())
