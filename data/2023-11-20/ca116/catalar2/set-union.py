#!/usr/bin/env python3

import sys

a = []
with open('a.txt', "r") as f:
  a = f.readlines()

b = []

with open('b.txt', "r") as f:
  b = f.readlines()

zo = {}

ma = 0
while ma < len(a):
  zo[a[ma].strip()] = "seen"
  ma += 1

mb = 0
while mb < len(b):
  if b[mb] not in zo:
    zo[b[mb].strip()] = "seen"
  mb += 1

zz = zo.keys()
AA = 0
while AA < len(zz):
  print(zo.keys()[AA])
  AA += 1
