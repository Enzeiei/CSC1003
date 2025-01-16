#!/usr/bin/env python3

sixshot = int(input())

hold = ((sixshot - ((sixshot // 10000) * 10000)) // 100)

print((hold // 10) + ((hold % 10) * 10))
