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
  track = 6
  while st < len(neon):
    check = True
    while check:
      read1 = neon[net][track:track + 2]
      read2 = neon[st][track:track + 2]
      if read1 == read2 and track >= 0:
        track -= 3
      else:
        check = False
        track = 6
      if read1 > read2:
        net = st
    st += 1
  tempest = neon[en]
  neon[en] = neon[net]
  neon[net] = tempest
  print(neon[en][9:])
  en += 1
if len(neon) >= 1:
  print(neon[en][9:])
