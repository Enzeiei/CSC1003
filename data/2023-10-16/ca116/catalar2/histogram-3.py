#!/usr/bin/env python3

stringer = input()
sets = len(stringer)

reiwa = 0
while reiwa < sets:
  print("*" * (int(stringer[reiwa])))
  reiwa += 1
