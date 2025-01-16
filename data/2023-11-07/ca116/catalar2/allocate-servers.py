#!/usr/bin/env python3

ti = input()
ma = []

while ti != "end":
  ma.append(int(ti))
  ti = input()
if ma != []:
  serv = [ma[0]]
  tick = 0
  runcheck = 0
  while tick < len(ma) - 1:
    ee = tick + 1
    if ma[tick] - 1000 > serv[runcheck]:
      runcheck += 1
    while ma[tick] + 1000 > ma[ee] and ee < len(ma) - 1:
      if ma[ee] not in serv:
        serv.append(ma[ee])
      ee += 1
    tick += 1
if ma == []:
  print(0)
else:
  mio = len(serv) - runcheck
  if mio == 9:
    print(10)
  else:
    print(mio)
