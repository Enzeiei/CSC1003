#!/usr/bin/env python3

inzie = input()
mayo = []

while inzie != "end":
  mayo.append(inzie)
  inzie = input()

ww = 1
while ww - 1 < len(mayo):
  print(mayo[-ww])
  ww += 1
