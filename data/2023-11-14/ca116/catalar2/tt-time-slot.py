#!/usr/bin/env python3

rei = []
claire = []
hell = input()

while hell != "end":
  rei = hell.split(" ")
  claire.append(rei)
  hell = input()

zhi = 0
thane = 0
while thane < len(claire):
  zhi = int(claire[thane][1]) + int(claire[thane][2])
  if zhi > 24:
    zhi -= 24
  claire[thane][1] = str(int(claire[thane][1])) + ":00"
  claire[thane][2] = str(zhi - 1) + ":50"
  print(" ".join(claire[thane]))
  thane += 1
