#!/usr/bin/env python3

import sys

ss = sys.stdin.read().split()

ss = " ".join(ss)
lii = 0

oo = 0
while oo + 1 < len(ss):
  if ss[oo] in [".", "!", "?"] and ss[oo + 1] == " ":
    print(ss[lii:oo + 1])
    lii = oo + 2
    oo += 1
  oo += 1

print(ss[lii:])
