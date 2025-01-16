#!/usr/bin/env python3

summit = 0

zenki = 0
while zenki < 10:
  tech = int(input())
  if tech < 0:
    tech *= -1
  summit += (tech % 10)
  zenki += 1

print(summit)
