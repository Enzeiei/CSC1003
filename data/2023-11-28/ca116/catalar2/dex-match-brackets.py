#!/usr/bin/env python3

import sys

st = sys.stdin.readlines()
# st = ["a = int('123')",
# "b = int)'123')",
# "c = "".join(lines[i].split())",
# "d = "".join(lines[i).split())",
# "e = "".join(lines[i].split()",
# "d = {}",
# "d[lines[len(lines) - i - 1]] = []",
# "d[lines[len_lines) - i - 1]] = []",
# "d[lines[len(lines) - i - 1]] =  ]",
# "d[lines[len(lines) - i - 1]) = []"]
oo = 0
# Priority System required.
get = {")": "(", "]": "[", "}": "{"}
grev = {"(": ")", "[": "]", "{": "}"}
gco = {")": 0, "]": 1, "}": 2}
while oo < len(st):
  # print(f"line {oo}")
  ac = st[oo].rstrip()
  # print(ac)
  # print(ac)
  tra = 0
  keeps = ""
  oak = []

  pri = {"(": 0, "[": 0, "{": 0}
  while tra < len(ac) and -1 not in list(pri.values()) and keeps == "":
    closer = ac[tra] in list(get.keys())
    if ac[tra] in pri:
      # print(tra, ac[tra])
      pri[ac[tra]] += 1
      oak.append(grev[ac[tra]])
    elif closer and len(oak) == 0 or closer and gco[ac[tra]] != gco[oak[-1]]:
      # print("kick", ac[tra], "not last in", oak)
      keeps = (f"{oo} {tra}")
    elif closer:
      # print(tra, ac[tra])
      pri[get[ac[tra]]] -= 1
      oak.pop()
    tra += 1
  pin = list(pri.values())
  if keeps != "":
    print(keeps)
  elif not (0 == pin[0] and 0 == pin[1] and 0 == pin[2]):
    # print(pri)
    print(oo, tra)
  oo += 1
