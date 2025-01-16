#!/usr/bin/env python3

binaria = input()
finalism = 0
extraction = len(binaria)

while extraction > 0:
  subject = int(binaria[-1 * extraction])
  finalism += subject * (2 ** (extraction - 1))
  extraction -= 1

print(finalism)
