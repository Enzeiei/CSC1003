#!/usr/bin/env python3

chariot = {}

steppes = int(input())

nul = 0
while nul < 5:
  stepper = int(input())
  if stepper > steppes:
    chariot[nul] = "higher"
  elif stepper == steppes:
    chariot[nul] = "equal"
  else:
    chariot[nul] = "lower"
  steppes = stepper
  nul += 1

repeater = 0
while repeater < 5:
  print(chariot[repeater])
  repeater += 1
