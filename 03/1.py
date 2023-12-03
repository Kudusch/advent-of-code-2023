#!/usr/bin/env python3

import re

# read input file
with open("example_input.txt", "r") as f:
    numbers = []
    gears = []
    schematic = []
    for i, l in enumerate(f.readlines()):
        schematic.append(list(l.strip()))
        numbers.extend([[i, match.span(), int(match.group())] for match in re.finditer(r"(\d+)", l.strip())])
        gears.extend([[i, match.span(), match.group()] for match in re.finditer(r"(\*)", l.strip())])

result = 0
for line, span, number in numbers:
    search_lines = []
    if line > 0:
        search_lines.append(schematic[line-1])
    search_lines.append(schematic[line])
    try:
        search_lines.append(schematic[line+1])
    except:
        pass
    
    start_span = max(span[0]-1, 0)
    end_span = span[1]+1

    for search_line in search_lines:
        if len(re.sub(r"[\d.]", "", "".join(search_line[start_span:end_span]))) > 0:
            result = result + number

print(f"Part 1: {result}")