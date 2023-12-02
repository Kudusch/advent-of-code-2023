#!/usr/bin/env python3

import re

limits = {"red":12, "green":13, "blue":14}

def make_dict(l):
    d = {}
    for e in l:
        v, k = e.split(" ")
        d[k] = int(v)
    return(d)

def is_game_possible(game):
    for subset in game:
        subset = make_dict(subset)
        for k, v in limits.items():
            if k in subset.keys() and subset[k] > v:
                return(False)
    return(True)

def get_power(game):
    game_limits = {"red":[], "green":[], "blue":[]}
    for subset in game:
        subset = make_dict(subset)
        for k in game_limits.keys():
            if k in subset.keys():
                game_limits[k].append(subset[k])
    power = 1
    for k, v in game_limits.items():
        power = power * max(v)
    return(power)

# read input file
with open("input.txt", "r") as f:
    games = []
    for game in f.readlines():
        game_id, subsets = game.strip().split(":")
        games.append([subset.strip().split(", ") for subset in subsets.strip().split(";")])

possible_games = 0
total_power = 0
for i, game in enumerate(games):
    total_power = total_power + get_power(game)
    if is_game_possible(game):
        possible_games = possible_games + i + 1

print(f"Part 1: {possible_games}")
print(f"Part 2: {total_power}")