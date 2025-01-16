#!/usr/bin/env python3

imp = input()

neon = []
while imp != "end":
  neon.append(imp)
  imp = input()

en = 0
tempest = 0
while en < len(neon) - 1:
  st = en
  net = en + 1
  while st < len(neon):
    if neon[net] > neon[st]:
      net = st
    st += 1
  tempest = neon[en]
  neon[en] = neon[net]
  neon[net] = tempest
  print(neon[en])
  en += 1
if len(neon) >= 1:
  print(neon[en])
