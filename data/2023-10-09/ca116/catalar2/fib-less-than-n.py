#!/usr/bin/env python3

seq = int(input())

fir = 0
sec = 1
print(fir)
print(sec)
while sec + fir < seq:
  print(fir + sec)
  sec, fir = (fir + sec), sec
