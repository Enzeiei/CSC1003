#!/usr/bin/env python3

sequencha = int(input())
x = 0
enzie = 1

print(x)

while enzie < sequencha:
  print(((-x + 1) * (x % 2)) + ((-x - 1) * ((x + 1) % 2)))
  enzie += 1
  x = (((-x + 1) * (x % 2)) + ((-x - 1) * ((x + 1) % 2)))
