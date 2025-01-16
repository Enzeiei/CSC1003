#!/usr/bin/env python3

buddha = input()
holder = ""

zz = True
annals = 0
while annals < len(buddha) and zz:
  scape = ord(buddha[annals])
  if scape >= 65 and scape <= 90:
    zz = False
  else:
    annals += 1

print(annals)
