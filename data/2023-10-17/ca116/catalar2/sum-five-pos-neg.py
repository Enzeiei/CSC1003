#!/usr/bin/env python3

nile = 0
judas = 0
zet = 0

zetto = 0
while zetto < 5:
  zet = int(input())
  if zet < 0:
    judas += zet
  else:
    nile += zet
  zetto += 1

print(judas, nile)
