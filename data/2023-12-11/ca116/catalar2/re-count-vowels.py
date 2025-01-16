#!/usr/bin/env python3

import sys

ss = sys.stdin.read().lower()
vow = {"a", "e", "i", "o", "u"}
tot = 0

o = 0
while o < len(ss):
  if ss[o] in vow:
    tot += 1
  o += 1

print(tot)
