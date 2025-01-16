#!/usr/bin/env python3

incr = int(input())
hail = int(input())

zets = 1
print(hail)

while zets < incr:

  if hail % 2 == 0:
    hail = (hail // 2)
  else:
    hail = ((hail * 3) + 1)

  print(hail)
  zets += 1
