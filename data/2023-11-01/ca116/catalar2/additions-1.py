#!/usr/bin/env python3


cycle = 0
while cycle < 10:
  ss = input()
  rr = 0
  while ss[rr] != "+":
    rr += 1
  print(int(ss[:rr]) + (int(ss[rr:])))
  cycle += 1
