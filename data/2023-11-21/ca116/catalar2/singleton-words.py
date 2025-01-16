#!/usr/bin/env python3

import sys

a = sys.stdin.read().strip().split()

ama = {}

o = 0
while o < len(a):
  if a[o] not in ama:
    ama[a[o]] = "!"
  elif a[o] in ama:
    ama[a[o]] = "?"
  o += 1

gund = list(ama.keys())

o = 0
while o < len(gund):
  if ama[gund[o]] == "!":
    print(gund[o])
  o += 1
