#!/usr/bin/env python3

import os
e = os.listdir(".")         # Line A.

i = 0
while i < len(e):
  if os.path.isfile(e[i]):
    with open(e[i], "r") as f:
      am = (f.read())
      if e[i][-4:] == ".bak" and am != "":
        os.unlink(e[i])
  i = i + 1
