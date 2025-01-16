#!/usr/bin/env python3

stringer = input()
repet = int(input())


enzed = (((stringer + "-") * repet))
print(enzed[:(len(enzed) - 1)])
