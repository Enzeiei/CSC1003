#!/usr/bin/env python3

import sys

a = sys.stdin.read().split()
ee = 0
mio = []
while ee < len(a):
  print(a[ee].split("/")[-1])
  ee += 1
