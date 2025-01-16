#!/usr/bin/env python3

import sys

# print(sys.argv[0])

toast = 0

args = sys.argv[1:]
emi = 0
a = []
b = []
while emi < len(args):
  with open(args[emi], "r") as f:
    if emi == 0:
      a = (f.read().split("\n"))
    else:
      b = (f.read().split("\n"))
  emi += 1
a.pop()
b.pop()
mi = 0
ca = 0
t1 = ""
t2 = ""
while ca < len(a) and ca < len(b) and t1 == t2:
  mi = 0
  while mi + 1 < len(a[ca]) and mi + 1 < len(b[ca]) and a[ca][mi] == b[ca][mi]:
    # print(a[ca][mi], b[ca][mi])
    mi += 1
  t1 = a[ca][mi]
  t2 = b[ca][mi]
  # print(len(a), len(b))
  ca += 1

if (ca <= len(a) or ca <= len(b)) and t1 != t2:
  print(ca - 1, mi)
elif t1 == t2 and len(a) != len(b):
  print(ca, 0)
