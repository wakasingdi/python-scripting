#!/usr/bin/env python3
import sys

args = sys.argv[1:]

#Detect if "--shout" flag is used
shout = False
if "--shout" in args:
    shout = True
    args.remove("--shout")

#Default names if none are provided
names = args if args else ["friend"]

#Greet each person
for name in names:
    greeting = f"Hello, {name}!"
    if shout:
        greeting = greeting.upper()
    print(greeting) 