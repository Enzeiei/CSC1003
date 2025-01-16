#!/usr/bin/env python3

imp = input()

neon = []
while imp != "end":
  neon.append(int(imp))
  imp = input()

st = 1
net = 0
while st < len(neon):
  if neon[net] > neon[st]:
    net = st
  st += 1

print(net)
