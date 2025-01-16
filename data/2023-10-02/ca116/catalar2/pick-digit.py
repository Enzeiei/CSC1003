#!/usr/bin/env python3

fours = int(input())
p = int(input())

print((fours % (10 ** (1 + p))) // (10 ** p))
