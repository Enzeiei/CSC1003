#!/usr/bin/env python3

import os
e = os.listdir(".")         # Line A.

i = 0
while i < len(e):
  holder = ""
  with open(e[i], "r") as f:
    am = (f.read())
    if e[i][-4:] != ".bak" and am != "":
      holder = am
  if holder != "":
    with open((e[i] + ".bak"), "w") as g:
      g.write(holder)
  i = i + 1
