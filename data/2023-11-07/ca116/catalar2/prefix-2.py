#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
  s = "mont"
cou = []
i = 0
while i < len(a):
  if a[i][0:len(s)] == s:
    cou.append(a[i])
  i += 1

if len(cou) != 0:
  print(cou[0])
