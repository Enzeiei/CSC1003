#!/usr/bin/env python3

stat = int(input())

zet = 0
while zet < 8:
  bonk = int(input())
  if bonk < stat:
    stat = bonk
  zet += 1

print(stat)
