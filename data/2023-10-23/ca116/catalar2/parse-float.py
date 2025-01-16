#!/usr/bin/env python3

star = input()

ss = 0
while ss < len(star) and star[ss] != ".":
  ss += 1

print(star[:ss])
print(star[ss + 1:])
