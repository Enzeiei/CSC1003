#!/usr/bin/env python3

import sys


convoy = sys.argv[1:]
# print(convoy)
line = convoy[0]
# print(line)
zeta = len(line)

zz = 0
LIP = 0   # Last important position
targ = 0
zo = ""
oz = " "

enc = ["://", ":", "/", "?", "#", ""]
ode = ["scheme:", "host:", "port:", "path:", "query-string:", "fragment-id:"]
while zz < zeta and targ < len(enc) - 1:
  zo = line[zz:zz + len(enc[targ])]
  # print(zo)
  if zo == (enc[targ]) or zo == (enc[targ + 1]):
    if ode[targ] != "path:":
      oz = " "
    else:
      oz = " /"
    print(ode[targ] + oz + line[LIP:zz])
    LIP = zz + len(enc[targ])
    zz += len(enc[targ]) - 1
    if zo == enc[targ + 1]:
      targ += 1
    targ += 1
  zz += 1
# print(line[LIP - 1], enc[targ - 1])
if line[LIP - 1] == enc[targ - 1]:
  if ode[targ] != "path:":
    oz = " "
  else:
    oz = " /"
  print(ode[targ] + oz + line[LIP:zeta])
