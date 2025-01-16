#!/usr/bin/env python3

if __name__ == "__main__":
   a = ["dog", "cat", "mouse"]

a[0], a[len(a) - 1] = a[len(a) - 1], a[0]
