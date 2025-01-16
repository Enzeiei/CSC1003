#!/usr/bin/env python3

topper = int(input())
zets = 1

while zets <= topper:

  fibi = zets

  if fibi % 3 == 0 and fibi % 5 == 0:
    print("fizz-buzz")

  elif fibi % 3 == 0:
    print("fizz")

  elif fibi % 5 == 0:
    print("buzz")

  else:
    print(fibi)

  zets += 1
