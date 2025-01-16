#!/usr/bin/env python3

sixshot = int(input())

print((sixshot - ((sixshot // 10000) * 10000)) // 100)
