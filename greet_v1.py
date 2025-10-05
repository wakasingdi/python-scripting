#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
	names = sys.argv[1:]
else:
	names = ["friend"]

for name in names:
	print(f"hello, {name}!")
