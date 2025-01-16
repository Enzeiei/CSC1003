#!/usr/bin/env python3

liner = int(input())
linetemp = liner

zett = 0
while zett < liner:
  print("*" * ((liner - (linetemp - zett) + 1)))
  zett += 1
