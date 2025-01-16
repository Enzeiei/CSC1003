#!/usr/bin/env python3

import os
e = os.listdir(".")
ind = 0

holder = "start.txt"
while os.path.isfile("./" + holder):
  ind = e.index(holder)
  if os.path.isfile(e[ind]):
    with open(e[ind], "r") as f:
      am = f.read().strip()
      if os.path.isfile("./" + am):
        holder = am
      else:
        print(am)
        holder = am
  else:
    print(am)
    holder = am
