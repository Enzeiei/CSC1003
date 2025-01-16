#!/usr/bin/env python3

lame = input()
lamao = ""
laman = len(lame)

rei = 0
while rei < laman:
  axiom = ord(lame[rei])
  if axiom >= 97 and axiom <= 122:
    lamao += chr(axiom - 32)
  else:
    lamao += lame[rei]
  rei += 1

print(lamao)
