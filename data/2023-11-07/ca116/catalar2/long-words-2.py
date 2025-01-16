#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["dog", "cat", "mouse"]

cc = []
i = 0
while i < len(a):
  if len(a[i]) >= 6:
    cc.append(a[i])
  i += 1

if len(cc) != 0:
  print(cc[0])
