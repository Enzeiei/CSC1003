#!/usr/bin/env python3

imp = input()

neon = []
while imp != "end":
  neon.append(int(imp))
  imp = input()

st = 1
net = neon[0]
while st < len(neon):
  if net > neon[st]:
    net = neon[st]
  st += 1

print(net)
