#!/usr/bin/env python3


tt = 0
while tt != 1000:
  zssa = input()
  tt = 0
  z1 = 0
  reader = 0
  while reader < len(zssa):
    if zssa[reader] == "+":
      tt += int(zssa[z1:reader])
      z1 = reader
    reader += 1

  tt += int(zssa[z1:reader])
  print(tt)
