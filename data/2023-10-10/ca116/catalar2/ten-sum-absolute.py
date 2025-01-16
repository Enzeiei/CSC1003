#!/usr/bin/env python3


total = 0

und = 0
while und < 10:
  ado = int(input())
  if ado < 0:
    ado *= -1
  total += ado
  und += 1

print(total)
