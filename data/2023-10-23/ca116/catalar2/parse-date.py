#!/usr/bin/env python3

s = input()

seq = ["", "", "", ""]

track1 = 0
c = False
zz = 0
while zz < len(s):
  if s[zz] == " ":
    c = False
    track1 += 1
  elif s[zz] != " ":
    c = True

  if c:
    seq[track1] += s[zz]
  zz += 1

print((seq[2])[:-1], seq[1] + ", " + seq[3] + " (" + seq[0] + ")")
