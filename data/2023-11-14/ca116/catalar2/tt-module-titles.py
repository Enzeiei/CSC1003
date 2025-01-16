#!/usr/bin/env python3

rei = []
claire = []
hell = input()

while hell != "end":
  rei = hell.split(" ")[5:]
  claire.append(rei)
  hell = input()

thane = 0
while thane < len(claire):
  print(" ".join(claire[thane]))
  thane += 1
