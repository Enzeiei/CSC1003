#!/usr/bin/env python3

mark = int(input())

print(f"first: {mark >= 70}\nsecond: {(70 > mark) and (mark >= 50)}")
print(f"third: {(50 > mark) and (mark >= 40)}\nfail: {40 > mark}")
