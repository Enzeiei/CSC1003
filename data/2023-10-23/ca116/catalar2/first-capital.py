#!/usr/bin/env python3

stt = input()

bumper = 0
while bumper < len(stt) and not(stt[bumper] >= "A" and stt[bumper] <= "Z"):
  bumper += 1

if bumper < len(stt):
  print(stt[bumper], bumper)
