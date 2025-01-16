#!/usr/bin/env python3

rei = []
claire = []
hell = input()

while hell != "end":
  rei = hell.split(" ")
  claire.append(rei)
  hell = input()

thane = 0
while thane < len(claire):
  if claire[thane][0] == "3":
    print(" ".join(claire[thane]))
  thane += 1
