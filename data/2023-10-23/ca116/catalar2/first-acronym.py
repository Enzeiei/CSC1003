#!/usr/bin/env python3

stt = input()

bumper = 0
while bumper < len(stt) and not(stt[bumper] >= "A" and stt[bumper] <= "Z"):
  bumper += 1

zoopa = bumper
while zoopa < len(stt) and (stt[zoopa] >= "A" and stt[zoopa] <= "Z"):
  zoopa += 1


if bumper < len(stt):
  print(stt[bumper:zoopa], bumper)
