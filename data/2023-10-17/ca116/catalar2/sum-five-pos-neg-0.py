#!/usr/bin/env python3

nile = 0
simon = 0

zet = int(input())
if zet < 0:
  simon += zet
else:
  nile += zet
while zet != 0:
  zet = int(input())
  if zet < 0:
    simon += zet
  else:
    nile += zet

print(simon, nile)
