#!/usr/bin/env python3

a = int(input())
b = int(input())

if a % 2 == 0:
  a = a // 2

else:
  a = (3 * a) + 1

if a == b:
  print("yes")

else:
  print("no")
