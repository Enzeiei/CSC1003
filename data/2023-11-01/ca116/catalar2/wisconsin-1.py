#!/usr/bin/env python3

inn = input()
inn = input()
while inn != "end":
  zz = 0
  p1 = 0
  p2 = 0
  comtrack = 0
  while zz < len(inn):
    if inn[zz] == ",":
      comtrack += 1
      if comtrack == 1:
        p1 = zz
      elif comtrack == 2:
        p2 = zz
    zz += 1
  if inn[p1 + 1:p2] == "WI":
    print(inn[:p1])
  inn = input()
