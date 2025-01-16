#!/usr/bin/env python3

aegis = int(input())
beta = int(input())

while beta != 0:
  aegis, beta = beta, aegis % beta

print(aegis)
