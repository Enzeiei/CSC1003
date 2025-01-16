#!/usr/bin/env python3

za = input()
re = []
chancer = 1

while za != "end":
  mm = 0
  chancer = 1
  while mm < len(re):
    if re[mm] == za:
      chancer = 0
    mm += 1
  if chancer == 1:
    re.append(za)

  za = input()

ee = 0
while ee < len(re):
  print(re[ee])
  ee += 1
