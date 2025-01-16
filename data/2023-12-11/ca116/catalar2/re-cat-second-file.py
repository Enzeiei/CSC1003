#!/usr/bin/env python3

import sys

a = sys.argv[1]
b = ""
with open(a, "r") as f:
  b = f.read()

with open(b, "r") as f:
  print(f.read().rstrip())
