#!/usr/bin/env python3

decinaria = int(input())
finalism = 0

highers = 10

while decinaria != 0 and highers >= 0:
  if (2 ** highers) <= decinaria:
    decinaria -= 2 ** highers
    finalism += 10 ** highers
  highers -= 1

print(finalism)
