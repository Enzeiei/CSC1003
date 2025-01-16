#!/usr/bin/env python3

inn = input()
inn = input()
hido = 0
p1 = 0
while inn != "end":
  z = 0
  while z + 3 < len(inn):
    if inn[z:z + 4] == "City":
      print(inn[:z + 4])
    z += 1
  inn = input()
