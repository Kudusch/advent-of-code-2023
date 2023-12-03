#!/usr/bin/env python3

import re

def extract_symbols(line):
    return [(match.group(), match.span()) for match in re.finditer(r"(\d+|[^.\d]+)", l.strip())]

def get_adj_numbers(anchor_span, i):
    adj_symbols = []
    adj_symbols.extend([symbol for symbol, span in schematic[max(i-1, 0)] if anchor_span[0] in range(span[0]-1, span[1]+1)])
    adj_symbols.extend([symbol for symbol, span in schematic[i] if anchor_span[0] in range(span[0]-1, span[1]+1)])
    adj_symbols.extend([symbol for symbol, span in schematic[i+1] if anchor_span[0] in range(span[0]-1, span[1]+1)])
    return [int(s) for s in adj_symbols if re.search(r"\d+", s)]

# read input file
with open("input.txt", "r") as f:
    schematic = []
    for i, l in enumerate(f.readlines()):
        schematic.append(extract_symbols(l))

result = 0
for i, symbols in enumerate(schematic):
    for symbol, span in symbols:
        if symbol == "*":
            adj_numbers = get_adj_numbers(span, i)
            if len(adj_numbers) == 2:
                result = result + (adj_numbers[0] * adj_numbers[1])

print(f"Part 2: {result}")
