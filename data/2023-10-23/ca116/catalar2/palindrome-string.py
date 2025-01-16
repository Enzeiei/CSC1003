#!/usr/bin/env python3

ss = input()

sslenh = len(ss) // 2

sz = 0
while sz < sslenh and ss[sz] == ss[-1 + (-sz)]:
  sz += 1

if sz >= sslenh:
  print("palindrome")
