#!/usr/bin/env python3

lin1 = input()
lin2 = input()
lin3 = input()

l1 = len(lin1)
l2 = len(lin2)
l3 = len(lin3)

if l1 > l2 and l1 > l3:
  print(lin1)

elif l2 > l1 and l2 > l3:
  print(lin2)

elif l3 > l1 and l3 > l2:
  print(lin3)
