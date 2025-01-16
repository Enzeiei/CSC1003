#!/usr/bin/env python3


zssa = input()
epi = []

while zssa != "end":
  point = 0
  teal = []
  find = 0
  while find < len(zssa):
    if zssa[find] == ",":
      teal.append(zssa[point:find])
      point = find + 1
    find += 1
  teal.append(zssa[point:find])
  epi.append(teal)
  zssa = input()

ent = int(input())

ww = 0
while ww < len(epi):
  print(epi[ww][ent])
  ww += 1
