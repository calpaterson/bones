import statistics
from itertools import combinations_with_replacement
from collections import Counter

import click
from yaml import safe_dump

from .cli import bones

def parse_dice(dice_string):
    """Parses a dice like 2d6 returning a list of outcomes"""
    n, d, sides = dice_string.partition("d")
    return [sum(o) for o in combinations_with_replacement(
        range(1, int(sides)+1), r=int(n)
    )]


def digest_outcomes(outcomes):
    digest = {
        "mean": statistics.mean(outcomes),
        "stddev": statistics.stdev(outcomes)
    }
    return digest


def print_histogram(outcomes):
    return_value = {}
    counter = Counter(outcomes)
    for outcome in sorted(counter.keys()):
        filled_key = str(outcome).rjust(3, " ")
        proportion = counter[outcome] / len(outcomes)
        bar_size = round(proportion * 79)
        # import pdb; pdb.set_trace()
        bar = "\u2588" * bar_size
        print("{}: {}".format(filled_key, bar))


@bones.command()
@click.argument("dice_string")
def dice(dice_string):
    outcomes = parse_dice(dice_string)
    print(
        safe_dump(
            digest_outcomes(outcomes),
            default_flow_style=False
        ))
    print_histogram(outcomes)
