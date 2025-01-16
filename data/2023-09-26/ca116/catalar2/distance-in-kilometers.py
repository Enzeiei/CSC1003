#!/usr/bin/env python3

meterlength = int(input())

print((((meterlength // 1000) * 1000) + (meterlength % 1000 * 2)) // 1000)
