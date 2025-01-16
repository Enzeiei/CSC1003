#!/usr/bin/env python3

import sys

ss = sys.stdin.readlines()

gaki = {}
oz = 0
while oz < len(ss) and True not in gaki.values():
  if ss[oz] not in gaki:
    gaki[ss[oz]] = False
  elif ss[oz] in gaki:
    gaki[ss[oz]] = True
    print(("snap: " + ss[oz]).strip())
  oz += 1
