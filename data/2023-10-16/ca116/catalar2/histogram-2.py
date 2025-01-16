#!/usr/bin/env python3

fullburn = {}
howmanymf = int(input())

rei = 0
while rei < howmanymf:
  fullburn[rei] = int(input())
  rei += 1

reiwa = 0
while reiwa < howmanymf:
  print(fullburn[reiwa] * "*")
  reiwa += 1
