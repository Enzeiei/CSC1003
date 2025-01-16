#!/usr/bin/env python3

import sys

geara = {}
ss = sys.stdin.read().split()

gaki = {
  "one": "eins",
  "two": "zwei",
  "three": "drei",
  "four": "vier",
  "five": "funf",
  "six": "sechs",
  "seven": "sieben",
  "eight": "acht",
  "nine": "neun",
  "ten": "zehn"
}

oz = 0
while oz < len(ss):
  if ss[oz] in gaki:
    print(gaki[ss[oz]])
  oz += 1
