#!/usr/bin/env python3

seq = int(input()) - 2

zets = 0
fir = 0
sec = 1
print(fir)
print(sec)

while zets < seq:
  print(fir + sec)
  sec, fir = (fir + sec), sec
  zets += 1
