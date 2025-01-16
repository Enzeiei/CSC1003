#!/usr/bin/env python3

self = input()
dot = False
dotp0 = False
negz = False
ss = 0

if self[0] == ".":
  dotp0 = True

if self[0:2] == "-.":
  self = "-0" + self[1:]

if self[-1] == ".":
  self += "0"

while ss < len(self):
  if self[ss] == ".":
    dot = True
  ss += 1

if dotp0:
  self = ("0" + self)

elif dot is False:
  self += ".0"

print(self)
