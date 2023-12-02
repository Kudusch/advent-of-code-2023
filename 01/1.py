#!/usr/bin/env python3

# read input file
with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

numbers = [str(n) for n in range(10)]

def get_calibration_value(l):
    lookup = [c in numbers for c in l]
    a = l[lookup.index(True)]
    lookup.reverse()
    l =  "".join([c for c in reversed(l)])
    b = l[lookup.index(True)]
    return(int(f"{a}{b}"))

result = 0
for l in lines:
    result = result + get_calibration_value(l)

print(result)