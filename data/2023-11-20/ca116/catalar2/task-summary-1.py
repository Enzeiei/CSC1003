#!/usr/bin/env python3

import sys

ss = sys.stdin.readlines()

ss0 = 0
while ss0 < len(ss):
  ss[ss0] = ss[ss0].strip().split(".")
  ss[ss0] = [(ss[ss0][0] + "." + ss[ss0][1]), ss[ss0][2]]
  ss0 += 1

stat = {}

ax = ""
m = ""
check = 0
while check < len(ss):
  ax = ss[check][0]
  m = ss[check][1]
  if ax not in stat:
    stat[ax] = m
  elif ax in stat and m != stat[ax]:
    stat[ax] = m
  check += 1

mewo = stat.keys()
aa = 0
while aa < len(mewo):
  if stat[mewo[aa]] == "correct":
    print(mewo[aa])
  aa += 1
