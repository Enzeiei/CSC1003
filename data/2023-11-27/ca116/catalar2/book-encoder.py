#!/usr/bin/env python3

import sys
import random as huh


# ru = input()
ru = sys.stdin.read()

ch = []

ii = 0
while ii < len(ru):
  get = ru[ii]
  extract = ""
  uo = []
  while extract == "":
    pincer = str(huh.randint(0, 9))
    name = "page-" + pincer + ".txt"
    red = []

    with open(name, "r") as f:
      mad = f.readlines()
      while len(red) != len(mad):
        co = huh.randint(0, len(mad))

        if co not in red:
          red.append(co)

          while extract == "" and co < len(mad):
            geki = 0

            while extract == "" and geki < len(mad[co]):
              if mad[co][geki] == get:
                extract = (f"{pincer} {co} {geki}")

              geki += 1
            co += 1
  if extract not in ch:
    ch.append(extract)
  else:
    ii -= 1
  ii += 1

aa = 0
while aa < len(ch):
  print(ch[aa])
  aa += 1
