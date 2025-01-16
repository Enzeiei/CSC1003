#!/usr/bin/env python3


total = 0

und = 0
while und < 10:
  ado = int(input())
  ado *= ((ado + 1) % 2)
  total += ado
  und += 1

print(total)
