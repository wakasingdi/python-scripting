#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
	name = sys.argv[1]
else:
	name = "friend"

print(f"Hello, {name}!")
