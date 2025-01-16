#!/usr/bin/env python3

import os
e = os.listdir(".")         # Line A.

sb = "#!/usr/bin/env python3"
i = 0
while i < len(e):
  with open(e[i], "r") as f:
    if (e[i][-3:] == ".py" and f.read() != "") or f.read()[:len(sb)] == sb:
      print(e[i])
  i = i + 1
