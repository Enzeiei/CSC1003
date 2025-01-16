#!/usr/bin/env python3

import sys

red = sys.argv[1:]
# print(red)

fr = {}
o = 0
while o < len(red):
  fr[red[o]] = len(red[o])
  o += 1
# print(fr)

rats = sys.stdin.read().split()
# rats = ["cat", "dog", "mouse", "elephant", "cherry"]

fo = 0
while fo < len(rats):
  if rats[fo] in list(fr.keys()):
    print(fr[rats[fo]] * "*")
  else:
    print(rats[fo])
  fo += 1
