#!/usr/bin/env python3

import re

# read input file
raw_cards = []
with open("input.txt", "r") as f:
    for l in f.readlines():
        winning, selected = re.sub(r"Card .*:", "", l).strip().split(" | ")
        raw_cards.append(([int(n) for n in re.split(r"\s+", winning) if n != ""], [int(n) for n in re.split(r"\s+", selected) if n != ""]))

result_1 = 0
cards = []
for i, (winning, selected) in enumerate(raw_cards):
    corrent_numbers_count = sum([n in winning for n in selected])
    cards.append(corrent_numbers_count)
    if corrent_numbers_count > 0:
        result_1 = result_1 + pow(2, corrent_numbers_count-1)

print(f"Part 1: {result_1}")

card_counts = [1]*len(cards)
for card_index in range(len(cards)):
    for j in range(cards[card_index]):
        for _ in range(card_counts[card_index]):
            card_counts[card_index+j+1] = card_counts[card_index+j+1] + 1

print(f"Part 2: {sum(card_counts)}")