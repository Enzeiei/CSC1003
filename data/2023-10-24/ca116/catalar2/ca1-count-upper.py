#!/usr/bin/env python3

s = input()
ll = len(s)
uppc = 0

z = 0
while z < ll:
  if s[z] >= "A" and s[z] <= "Z":
    uppc += 1
  z += 1

print(uppc)
