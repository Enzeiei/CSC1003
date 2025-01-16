#!/usr/bin/env python3

fibi = int(input())

if fibi % 3 == 0 and fibi % 5 == 0:
  print("fizz-buzz")

elif fibi % 3 == 0:
  print("fizz")

elif fibi % 5 == 0:
  print("buzz")

else:
  print(fibi)
