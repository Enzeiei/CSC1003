#!/usr/bin/env python3

stat = int(input())

zet = 0
while zet < 9:
  put = int(input())
  if put % 2 != 0:
    pass
  elif put < stat:
    stat = put

  zet += 1

print(stat)
