#!/usr/bin/env python3

import sys

# print(sys.argv[0])

toast = 0

args = sys.argv[1:]
emi = 0
while emi < len(args):
  with open(args[emi], "r") as f:
    a = (f.read().rstrip()).split()
    e = 0
    while e < len(a):
      toast += int(a[e])
      e += 1
  emi += 1
print(toast)
