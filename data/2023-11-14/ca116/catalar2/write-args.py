#!/usr/bin/env python3

import sys

# print(sys.argv[0])

filer = sys.argv[1]

# Reading files...

file_name = filer

with open(file_name, "w") as f:
  # f as the file obj for writing this shit to
  f.write("\n".join(sys.argv[2:]) + "\n")
