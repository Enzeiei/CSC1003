#!/usr/bin/env python3

stat = int(input())

zet = 0
while zet < 9:
  bonk = int(input())
  if bonk <= 0:
    bonk = bonk
  elif bonk < stat:
    stat = bonk
  zet += 1

print(stat)
