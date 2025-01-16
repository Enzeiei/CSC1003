#!/usr/bin/env python3

tanker = 0

zenki = 0
while zenki < 10:
  tanker += int(input()) * (10 ** zenki)
  zenki += 1

tylenol = 10
while tylenol > 0:
  print(tanker % (10 ** tylenol) // 10 ** (tylenol - 1))
  tylenol -= 1
