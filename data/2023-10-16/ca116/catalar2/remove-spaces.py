#!/usr/bin/env python3

stringer = input()
sets = len(stringer)
mt = ""
rei = 0
while rei < sets:
  if stringer[rei] != " ":
    mt += stringer[rei]
  rei += 1
print(mt)
