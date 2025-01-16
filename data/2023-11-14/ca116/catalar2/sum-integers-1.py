#!/usr/bin/env python3

import sys

a = sys.stdin.read().split()
toast = 0
e = 0
while e < len(a):
  toast += int(a[e])
  e += 1

print(toast)
