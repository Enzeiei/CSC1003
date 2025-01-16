#!/usr/bin/env python3

args = "irish-dobs.txt"


with open(args, "r") as f:
  m = (f.readlines())
  ro = 0
  tp = []
  xs = []
  while ro < len(m):
    tp = m[ro].split()[0]
    xs = m[ro].split()[1:]
    tp = tp.split("/")
    #print(tp)
    tp[0], tp[1] = tp[1], tp[0]
    m[ro] = (("/".join(tp)) + " " + " ".join(xs))
    ro += 1

with open("american-dobs.txt", "w") as f:
  f.write("\n".join(m) + "\n")
