#!/usr/bin/env python3

fullburn = {}

rei = 0
while rei < 10:
  fullburn[rei] = int(input())
  rei += 1

reiwa = 0
while reiwa < 10:
  print(fullburn[reiwa] * "*")
  reiwa += 1
