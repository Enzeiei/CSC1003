#!/usr/bin/env python3

l1 = int(input())
l2 = int(input())
l3 = int(input())

if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l2 + l1):
  print("yes")

else:
  print("no")
