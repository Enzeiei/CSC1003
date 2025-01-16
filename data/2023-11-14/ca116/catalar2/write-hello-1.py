#!/usr/bin/env python3

# Reading files...

file_name = "hello.txt"

with open(file_name, "w") as f:
  # f as the file obj for writing this shit to
  f.write("Hello world.\n")
