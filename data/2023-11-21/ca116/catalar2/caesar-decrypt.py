#!/usr/bin/env python3

import sys

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lower_rot = lower[n:] + lower[:n]
upper_rot = upper[n:] + upper[:n]

d = {}
i = 0
while i < len(lower):
  d[lower_rot[i]] = lower[i]
  d[upper_rot[i]] = upper[i]
  i += 1

s = sys.stdin.read()
t = []
# inefficient here
i = 0
while i < len(s):
  if s[i] in d:
    # t += d[s[i]]
    t.append(d[s[i]])
  else:
    # t += s[i]
    t.append(s[i])
  i += 1
print("".join(t).strip())
