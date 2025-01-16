#!/usr/bin/env python3

decinaria = int(input())
finalism = ""
runner = ""
remnant = 0
overhead = ["a", "b", "c", "d", "e", "f"]

highers = 0
while 16 ** highers <= decinaria:
  highers += 1


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


z = 0
while z < len(finalism) and not(finalism[z] >= "a" and finalism[z] <= "f"):
  z += 1

if z < len(finalism):
  print(finalism[z])
