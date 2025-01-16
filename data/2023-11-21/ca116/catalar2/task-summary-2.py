#!/usr/bin/env python3

import sys

ss = sys.stdin.readlines()

k = 0
while k < len(ss):
  ss[k] = ss[k].strip().split("/")
  ss[k][1] = ss[k][1].split(".")
  ss[k][1] = [(ss[k][1][0] + "." + ss[k][1][1]), ss[k][1][2]]
  k += 1

stat = {}
ax = ""
m = ""
x = ""
check = 0
while check < len(ss):
  ax = ss[check][0]
  x = ss[check][1][0]
  m = ss[check][1][1]
  if ax not in stat:
    stat[ax] = {}
    (stat[ax])[x] = m
  elif ax in stat:
    (stat[ax])[x] = m
  check += 1

ga = list(stat.keys())
n = 0
while n < len(ga):   # use each key
  inn = 0
  ikea = list(stat[ga[n]].keys())
  # print(ga[n], ikea)
  aha = 0
  while inn < len(ikea):  # going through each users comp
    if stat[ga[n]][ikea[inn]] == "correct":
      aha += 1
    inn += 1
  print(ga[n], aha)
  n += 1
