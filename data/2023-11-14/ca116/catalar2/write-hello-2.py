#!/usr/bin/env python3

import sys

# print(sys.argv[0])

args = sys.argv[1]

# Reading files...

file_name = args

with open(file_name, "w") as f:
  # f as the file obj for writing this shit to
  f.write("Hello world.\n")
