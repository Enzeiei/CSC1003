#!/usr/bin/env python3

import sys

lines = []
with open('translation.txt', "r") as f:
    lines = f.readlines()

eos = []
gaki = {}
aa = 0
while aa < len(lines):
  eos = (lines[aa]).split()
  gaki[eos[0]] = [eos[1]][0]
  aa += 1

ss = sys.stdin.read().split()

oz = 0
while oz < len(ss):
  if ss[oz] in gaki:
    print(gaki[ss[oz]])
  oz += 1
