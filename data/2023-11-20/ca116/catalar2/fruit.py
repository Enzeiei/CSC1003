#!/usr/bin/env python3

import sys

geara = {}
ss = sys.stdin.read().split()

fruit = {
  "apple": True,
  "pear": True,
  "orange": True,
  "banana": True,
  "cherry": True,
}

oz = 0
while oz < len(ss):
  if ss[oz] in fruit:
    print(ss[oz])
  oz += 1
