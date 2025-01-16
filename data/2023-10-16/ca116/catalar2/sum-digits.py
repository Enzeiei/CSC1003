#!/usr/bin/env python3

stringer = input()
sets = len(stringer)

fullburn = 0
reiwa = 0
while reiwa < sets:
  fullburn += int(stringer[reiwa])
  reiwa += 1

print(fullburn)
