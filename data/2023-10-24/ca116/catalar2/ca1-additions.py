#!/usr/bin/env python3

s = input()
tempest = 0
while s != "end":
  mio = 0
  while mio < len(s) and s[mio] != " ":
    mio += 1
  a = (s[:(mio)])
  b = (s[mio + 1:])
  leadin = 16 - (len(a) + len(b))
  tale = str(int(a) + int(b))
  print((leadin * " ") + a + " + " + b + " = " + tale)
  s = input()
