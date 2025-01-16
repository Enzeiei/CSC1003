#!/usr/bin/env python3

stringer = input()
sets = len(stringer)
mt = ""

mt = (stringer[sets - 1] + stringer[1:sets - 1] + stringer[0])
print(mt)
