#!/usr/bin/env python3

ks = ""

with open("characters.txt", "r") as f:
  ks = f.read()

i = 0
while i < len(ks):
  if ks[i] == "\n":
    print()
  else:
    print(ks[i])
  i += 1
