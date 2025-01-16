#!/usr/bin/env python3

import sys

# with open("code.txt", "r") as f:
# ll = f.read().split()
ll = sys.stdin.read().split()

full = ""
gat = 3

aa = 0
while aa < (len(ll) // gat):
  point = aa * gat
  set = [ll[point], int(ll[point + 1]), int(ll[point + 2])]
  name = "page-" + set[0] + ".txt"

  with open(name, "r") as f:
    mad = f.readlines()
    full += mad[set[1]][set[2]]

  aa += 1

print(full[:-1])
