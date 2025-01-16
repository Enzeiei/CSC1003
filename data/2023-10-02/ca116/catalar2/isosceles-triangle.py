#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

print((a == (b or c)) or (b == (c or a)) or (c == (a or b)))
