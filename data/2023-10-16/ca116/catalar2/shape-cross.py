#!/usr/bin/env python3

liner = int(input())
linetemp = (liner // 2)

zett = 0
while zett < liner:
  if linetemp == zett:

    print("*" * liner)
  else:

    print((" " * linetemp) + "*")

  zett += 1
