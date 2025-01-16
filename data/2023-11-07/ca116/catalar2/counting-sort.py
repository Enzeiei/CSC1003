#!/usr/bin/env python3

rr = input()
mio = []
dupen = []
dc = []
while rr != "end":
  if rr.isdigit():
    if int(rr) in mio and int(rr) not in dupen:
      dupen.append(int(rr))
      dc.append(2)
    elif int(rr) in mio and int(rr) in dupen:
      dc[dupen.index(int(rr))] += 1
    elif int(rr) not in mio and int(rr) not in dupen:
      mio.append(int(rr))
  rr = input()

aa = 0
ha = 0
while ha < 999:
  if ha in mio and ha not in dupen:
    print(ha)
  elif ha in mio and ha in dupen:
    print(((str(ha) + "\n") * (dc[dupen.index(ha)]))[:-1])
  ha += 1
