#!/usr/bin/env python3

import sys

ss = sys.stdin.read().split()

ss = " ".join(ss)
lii = 0
stemp = ""
def change(n):
  # print(n[0])
  if n[0] >= "a" and n[0] <= "z":
    return (chr(ord(n[0]) - 32)) + n[1:]
  else:
    return (n)


oo = 0
while oo + 1 < len(ss):
  if ss[oo] in [".", "!", "?"] and ss[oo + 1] == " ":
    stemp = (ss[lii:oo + 1])
    print(change(stemp))
    lii = oo + 2
    oo += 1
  oo += 1

stemp = (ss[lii:])
print(change(stemp))
