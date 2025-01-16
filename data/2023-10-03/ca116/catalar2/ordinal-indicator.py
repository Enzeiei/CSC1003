#!/usr/bin/env python3

datum = int(input())

if datum % 100 in {11, 12, 13}:
  print("th")

elif datum % 10 == 1:
  print("st")

elif datum % 10 == 2:
  print("nd")

elif datum % 10 == 3:
  print("rd")

else:
  print("th")
