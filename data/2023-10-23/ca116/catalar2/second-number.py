#!/usr/bin/env python3

stt = input()

bumper = 0
zoopa = 0
stat = 0
while stat <= 1:
  bumper = zoopa
  while bumper < len(stt) and not(stt[bumper] >= "0" and stt[bumper] <= "9"):
    bumper += 1

  zoopa = bumper
  while zoopa < len(stt) and (stt[zoopa] >= "0" and stt[zoopa] <= "9"):
    zoopa += 1
  stat += 1

if stat == 2 and zoopa != bumper:
  print(stt[bumper:zoopa], bumper)
