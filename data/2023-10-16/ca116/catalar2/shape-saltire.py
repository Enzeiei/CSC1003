#!/usr/bin/env python3

liner = int(input())
linetemp = liner
lmid = liner // 2

zett = 0

while zett < liner:
  if zett < lmid:
    print((" " * zett) + "*" + (" " * (liner - (zett * 2) - 2)) + "*")
  elif zett == lmid:
    print((" " * lmid) + "*")
  else:
    print((" " * (liner - (zett) - 1)) + "*" + (" " * (((zz) * 2) - 1)) + "*")
  zett += 1
  zz = zett - lmid
