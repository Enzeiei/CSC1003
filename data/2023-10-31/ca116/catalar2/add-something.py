#!/usr/bin/env python3

enter = input()
gund = []

whar = 0
while enter != "end":
  gund.append(int(enter))
  enter = input()
  whar += 1
ww = int(input())

zz = 0
while zz < whar:
  print(gund[zz] + ww)
  zz += 1
