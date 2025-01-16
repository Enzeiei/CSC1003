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
  print(a[ma])
  zo[a[ma].strip()] = "?"
  ma += 1

mb = 0
while mb < len(b):
  print(b[mb])
  if b[mb] in zo.keys():
    print("!")
    zo[b[mb].strip()] = "!"
  mb += 1

zz = zo.keys()
AA = 0
while AA < len(zz):
  # print(zz[AA], zo[zz[AA]])
  if zo[zz[AA]] == "!":
    print(zz[AA])
  AA += 1
