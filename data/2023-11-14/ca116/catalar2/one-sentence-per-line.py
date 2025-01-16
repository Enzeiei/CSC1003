#!/usr/bin/env python3

claire = []
tempclaire = []
ray = []

ars = input()
runner = 0
while ars != "end":
  tempclaire = (ars.split(" "))
  mio = 0
  while mio < len(tempclaire):
    if tempclaire[mio] != "" and "." in tempclaire[mio]:
      runner = 0
      while runner < len(tempclaire[mio]):
        if tempclaire[mio][runner] == ".":
          ray.append(tempclaire[mio][:runner + 1])
          claire.append(ray)
          ray = []
          if tempclaire[mio][runner + 1:] != "":
            ray.append(tempclaire[mio][runner + 1:])
        runner += 1
    elif tempclaire[mio] != "":
      ray.append(tempclaire[mio])
    mio += 1
  ars = input()

if ray != []:
  claire.append(ray)

hot_rod = 0
while hot_rod < len(claire):
  print(" ".join(claire[hot_rod]))
  hot_rod += 1
