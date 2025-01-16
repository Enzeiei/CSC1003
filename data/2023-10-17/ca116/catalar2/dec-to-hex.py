#!/usr/bin/env python3

decinaria = int(input())
finalism = ""
runner = ""
remnant = 0
overhead = ["a", "b", "c", "d", "e", "f"]
highers = 5

while highers >= 0:
  if (16 ** highers) < decinaria:
    valza = decinaria // (16 ** (highers))
    remnant = decinaria % 16 ** highers
    if valza >= 10:
      runner = overhead[(valza - 10)]
    else:
      runner = str(valza)
    finalism += runner
    decinaria = remnant
  elif decinaria == 0:
    finalism += "0"
  highers -= 1

print(finalism)
