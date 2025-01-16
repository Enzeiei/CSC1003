#!/usr/bin/env python3

import sys

ll = sys.stdin.read().split()
# ll = ["Classroom", "Vowel", "61", "Object", "Car", "63"]

tf = {}
valsie = []
ava = 0

gat = 3
o = 0
while o < (len(ll) // gat):
  num = int(ll[(o * gat) + 2])
  valsie.append(num)
  tf[(ll[o * gat] + " " + ll[(o * gat) + 1])] = num
  o += 1

vc = 0
while vc < len(valsie):
  ava += valsie[vc]
  vc += 1

ava //= len(valsie)
# print(ava)
seek = list(tf.keys())

final = 0
while final < len(seek):
  if tf[seek[final]] > ava:
    print(seek[final])
  final += 1
