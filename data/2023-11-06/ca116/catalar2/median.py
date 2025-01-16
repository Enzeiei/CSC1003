#!/usr/bin/env python3

imp = input()

neon = []
while imp != "end":
  neon.append(int(imp))
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
  en += 1

t1 = len(neon) // 2
t2 = len(neon) / 2
if t1 == t2:
  if neon[t1 - 1] > neon[t1]:
    print(neon[t1 - 1])
  else:
    print(neon[t1])
else:
  print(neon[t1])
