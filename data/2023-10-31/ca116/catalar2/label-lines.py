#!/usr/bin/env python3

enter = input()
gund = []

tipp = 0
while enter != "end":
  gund.append(enter)
  enter = input()
  tipp += 1

zz = 0
while zz < tipp:
  print(zz, tipp, gund[zz])
  zz += 1
