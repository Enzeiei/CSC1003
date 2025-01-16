#!/usr/bin/env python3

import sys

b = []
with open('boys.txt', "r") as f:
  b = f.read().strip().split()

g = []

with open('girls.txt', "r") as f:
  g = f.read().strip().split()

na = sys.stdin.read().strip().split()

o = 0
while o < len(na):
  # print(na[o])
  if na[o] in b and na[o] in g:
    print(na[o], "either")
  elif na[o] in b:
    print(na[o], "boy")
  elif na[o] in g:
    print(na[o], "girl")
  o += 1
