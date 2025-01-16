#!/usr/bin/env python3

chariot = {}

steppes = int(input())

nul = 0
while steppes != 0:
  stepper = int(input())
  if stepper > steppes:
    chariot[nul] = "higher"
  elif stepper == steppes:
    chariot[nul] = "equal"
  elif stepper < steppes:
    chariot[nul] = "lower"
  steppes = stepper
  nul += 1

repeater = 0
while repeater < (nul - 1):
  print(chariot[repeater])
  repeater += 1
