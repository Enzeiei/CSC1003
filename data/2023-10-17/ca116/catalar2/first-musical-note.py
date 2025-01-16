#!/usr/bin/env python3

buddha = input()
holder = ""

zz = True
annals = 0
while annals < len(buddha) and zz:
  scape = ord(buddha[annals])
  if scape >= 97 and scape <= 103:
    holder = buddha[annals]
    zz = False
  annals += 1

print(holder)
