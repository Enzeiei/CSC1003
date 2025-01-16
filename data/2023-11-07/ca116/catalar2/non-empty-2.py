#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["dog", "cat", "mouse"]

counter = []
i = 0
while i < len(a):
  if a[i] != "":
    counter.append(a[i])
  i += 1
if len(counter) != 0:
  print(counter[0])
