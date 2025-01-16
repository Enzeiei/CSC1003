#!/usr/bin/env python3

import os
e = os.listdir(".")         # Line A.

i = 0
while i < len(e):
  with open(e[i], "r") as f:
    if e[i][-3:] == ".py" and f.read() != "":       # Line B.
      print(e[i])
  i = i + 1
