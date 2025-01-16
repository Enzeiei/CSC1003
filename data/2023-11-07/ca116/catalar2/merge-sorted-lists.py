#!/usr/bin/env python3

e0 = []
e1 = []
inc = 0
while inc < 2:
  ss = input()
  while ss != "end":
    if inc == 0:
      e0.append(int(ss))
    else:
      e1.append(int(ss))
    ss = input()
  inc += 1

i = 0
j = 0
while i < len(e0) and j < len(e1):
  if e0[i] < e1[j]:
    print(e0[i])
    i += 1
  elif e0[i] > e1[j]:
    print(e1[j])
    j += 1
  else:
    print(e0[i])
    print(e1[j])
    i += 1
    j += 1
while i >= len(e0) and j < len(e1):
  print(e1[j])
  j += 1
while j >= len(e1) and i < len(e0):
  print(e0[i])
  i += 1
