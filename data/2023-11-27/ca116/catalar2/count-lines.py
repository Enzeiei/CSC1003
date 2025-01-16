#!/usr/bin/env python3

import sys

why = sys.stdin.readlines()
a = list(map(int, why[0][:-1].split()))
b = list(map(int, why[1][:-1].split()))
c = list(map(int, why[2][:-1].split()))

def pinna(va, se):
  if (va) > (se[-1]):
    print(f"{va} > {se[-1]}")
    return -1
  else:
    low = 0
    high = len(se)
    while low < high:
      mid = (low + high) // 2
      if int(se[mid]) < va:
        # print(f"{va} over {a[mid]}")
        low = mid + 1
        # assert low == 0 or a[low-1] < q
      else:
        # print(f"{va} under {a[mid]}")
        high = mid
        # assert high == len(a) or q <= a[high]
    if high >= len(se):
      return len(se) - 1
    else:
      return high


tot = 0
mm = 0
while mm < len(a):
  ami = a[mm]
  stepr = 0
  while ami + (stepr * 2) <= int(c[-1]):
    f = ami + stepr
    g = ami + (stepr * 2)
    # print(f"For {ami}, need {f} and {g}.")
    # print(pinna(g, c))
    if f == b[pinna(f, b)] and g == c[pinna(g, c)]:
      tot += 1
    stepr += 1
  stepr = 1
  while ami - (stepr * 2) >= int(c[0]):
    f = ami - stepr
    g = ami - (stepr * 2)
    if f == b[pinna(f, b)] and g == c[pinna(g, c)]:
      tot += 1
    stepr += 1
  mm += 1
print(tot)
