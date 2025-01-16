#!/usr/bin/env python3

stt = input()

bumper = 0
while bumper < len(stt) and not(stt[bumper] >= "0" and stt[bumper] <= "9"):
  bumper += 1

zoopa = bumper
while zoopa < len(stt) and (stt[zoopa] >= "0" and stt[zoopa] <= "9"):
  zoopa += 1


if bumper < len(stt):
  print(stt[bumper:zoopa], bumper)
