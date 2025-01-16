#!/usr/bin/env python3

n_type = int(input())

z = 0
while z < n_type:
  n = int(input())
  if n % 2 != 0:
    print(n)
  z += 1
