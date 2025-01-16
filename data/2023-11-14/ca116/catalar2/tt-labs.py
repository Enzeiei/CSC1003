#!/usr/bin/env python3

rei = []
claire = []
hell = input()

while hell != "end":
  rei = hell.split(" ")
  claire.append(rei)
  hell = input()

lenee = 0

thane = 0
while thane < len(claire):
  if int(claire[thane][2]) >= 2:
    print(" ".join(claire[thane]))
  thane += 1
