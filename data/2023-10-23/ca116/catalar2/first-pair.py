#!/usr/bin/env python3

s = input()

zz = 0
ff = True
while zz + 1 < len(s) and ff:
  zz += 1
  if s[zz] == s[zz - 1]:
    ff = False

if not ff:
  print(s[zz] + s[zz - 1])
