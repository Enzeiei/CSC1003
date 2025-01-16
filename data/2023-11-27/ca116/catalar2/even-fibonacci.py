#!/usr/bin/env python3

import sys


seq = int(sys.argv[1])

mad = 0
huo = []
fir = 0
sec = 1
while sec + fir < seq:
  sec, fir = (fir + sec), sec
  # print(fir, sec)
  if fir % 2 == 0 and (fir not in huo):
    mad += fir
    # print("be")
    huo.append(fir)
  if sec % 2 == 0 and (sec not in huo):
    mad += sec
    # print("he")
    huo.append(sec)

print(mad)
