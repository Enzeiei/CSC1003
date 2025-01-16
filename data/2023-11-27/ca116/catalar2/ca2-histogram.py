#!/usr/bin/env python3

import sys

def bar():
  print(" " + ("-" * 23))


num = sys.stdin.read().split()
block = {}

a = 0
while a < len(num):
  if num[a] not in block:
    block[num[a]] = 1
  else:
    block[num[a]] += 1
  a += 1
ja = {}
sa = list(block.values())
gat = 0
a = 0

def jg(j, g, t):
  if t == 0 and g not in j:
    j[g] = 1
  elif t == 0 and g in j:
    j[g] += 1
  elif g not in j and (g + 1) in j:
    j[g] = j[g + 1]
  elif g in j:
    j[g] += 1


a = 0
while a < len(sa):
  if sa[a] > gat:
    gat = sa[a]
    jg(ja, gat, 0)
    ss = 0
    while ss < gat:
      jg(ja, gat - ss, 1)
      ss += 1
  else:
    ss = 0
    while ss < sa[a]:
      jg(ja, sa[a] - ss, 0)
      ss += 1
  a += 1

a = 0
while a < gat:
  vgat = gat - a
  me = " | "
  dd = 0
  count = 1
  while dd < 20 and count < ja[vgat]:
    if str(dd) in block and block[str(dd)] >= vgat:
      me += "*"
      count += 1
    else:
      me += " "
    dd += 1
  print(me)
  a += 1
bar()
