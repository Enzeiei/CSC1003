#!/usr/bin/env python3

weigh = int(input())
height = int(input())

bmi = weigh / (height * height) * 10000

if bmi > 30:
  print("obese")

elif bmi > 25:
  print("overweight")

elif bmi > 18.5:
  print("normal")

else:
  print("underweight")
