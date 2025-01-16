#!/usr/bin/env python3

stringer = input()
sets = len(stringer)
mt = ""

rei = 0
while rei < sets:
  mt += (stringer[sets - rei - 1])
  rei += 1

print(mt)
