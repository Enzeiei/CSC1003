#!/usr/bin/env python3

import os
e = os.listdir(".")
ef = len(e)
st = "./"

def incurr(a, pn):
  axiom = (a + pn + "/")
  li = os.listdir(axiom)
  p0 = 0
  while p0 < len(li):
    # print(axiom, li[p0])
    if os.path.isfile(axiom + li[p0]):
      print(axiom + li[p0])
    elif os.path.isdir(axiom + li[p0]):
      # print(li[p0] + "bad!!")
      incurr(axiom, li[p0])
    p0 += 1


incurr(".", "")
