#!/usr/bin/env python3

lame = input()
lamao = ""
laman = len(lame)
switcher = 2


rei = 0
while rei < laman:
  axiom = ord(lame[rei])
  if axiom >= 65 and axiom <= 90 and (switcher in {0, 2, 3}):
    lamao += chr(axiom + 32)
    switcher = 1
  elif axiom >= 97 and axiom <= 122 and (switcher in {1, 3}):
    lamao += chr(axiom - 32)
    switcher = 0
  elif axiom >= 65 and axiom <= 90 or axiom >= 97 and axiom <= 122:
    lamao += lame[rei]
    if switcher == 1:
      switcher = 0
    else:
      switcher = 1
  else:
    lamao += lame[rei]
  rei += 1

print(lamao)
