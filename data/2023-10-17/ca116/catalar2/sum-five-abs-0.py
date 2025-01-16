#!/usr/bin/env python3

nile = 0

zet = int(input())
if zet < 0:
  zet *= -1
while zet != 0:
  nile += zet
  zet = int(input())
  if zet < 0:
    zet *= -1

print(nile)
