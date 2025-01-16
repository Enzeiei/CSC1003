#!/usr/bin/env python3

tanker = int(input())

ty = 0
nutank = tanker
while nutank != 0:
  nutank //= 10
  ty += 1

sectank = 0

pa = ty
while ty > 0:
  sectank += (tanker % (10 ** ty)) // (10 ** (ty - 1)) * (10 ** (pa - ty))
  ty -= 1

if tanker == sectank:
  print("yes")

else:
  print("no")
