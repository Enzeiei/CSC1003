#!/usr/bin/env python3

rio = []
eve = []
ee = input()
while ee != "end":
  if int(ee) % 2 == 1:
    rio.append(ee)
  else:
    eve.append(ee)

  ee = input()

zz = 0
while zz < len(rio) + len(eve):
  if zz < len(eve):
    print(eve[zz])
  else:
    print(rio[zz - len(eve)])

  zz += 1
