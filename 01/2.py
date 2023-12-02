#!/usr/bin/env python3

import re

# read input file
with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
r_1 = r"(\d|" + "|".join(numbers) + ")"
r_2 = r"(\d|" + "|".join([n[::-1] for n in numbers]) + ")"
result = 0

for l in lines:
    a = re.findall(r_1, l)[0]
    b = re.findall(r_2, l[::-1])[0]
    if a in numbers:
        a = numbers.index(a)+1
    if b in [n[::-1] for n in numbers]:
        b = [n[::-1] for n in numbers].index(b)+1
    result = result + int(f"{a}{b}")

print(result)