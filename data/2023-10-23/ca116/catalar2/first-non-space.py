#!/usr/bin/env python3

stt = input()

bumper = 0
while bumper < len(stt) and (stt[bumper] == " "):
  bumper += 1

if bumper < len(stt):
  print(bumper)
else:
  print(-1)
