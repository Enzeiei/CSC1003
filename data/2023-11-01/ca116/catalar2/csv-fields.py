#!/usr/bin/env python3

inn = input()

za = 0
ss = 0
while za < len(inn):
  if inn[za] == ",":
    print(inn[ss:za])
    ss = za + 1
  za += 1
print(inn[ss:za])

ra = True
while ra:
  ra = False
