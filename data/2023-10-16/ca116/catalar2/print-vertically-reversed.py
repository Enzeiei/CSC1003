#!/usr/bin/env python3

stringer = input()
sets = len(stringer)

rei = 0
while rei < sets:
  print(stringer[sets - rei - 1])
  rei += 1
