#!/usr/bin/env python3

liner = int(input())

print("*" * liner)

zett = 0
while zett < (liner - 2):
  print("*" + " " * (liner - 2) + "*")
  zett += 1

if liner != 1:
  print("*" * liner)
