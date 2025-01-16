#!/usr/bin/env python3

zz = input()
nu = []

while zz != "end":
  nu.append(int(zz))
  zz = input()

dots = 0
while dots <= 9:
  setter = 0
  re = 0
  while re < len(nu):
    if nu[re] == dots:
      setter += 1
    re += 1
  print(dots, "*" * setter)
  dots += 1
