import statistics
from itertools import combinations_with_replacement

import click
from yaml import safe_dump

from .cli import bones

def parse_dice(dice_string):
    """Parses a dice like 2d6 returning a list of outcomes"""
    n, d, sides = dice_string.partition("d")
    return set(sum(o) for o in combinations_with_replacement(
        range(1, int(sides)+1), r=int(n)
    ))


def digest_outcomes(outcomes):
    return {
        "mean": statistics.mean(outcomes),
        "stddev": statistics.stdev(outcomes)
    }


@bones.command()
@click.argument("dice_string")
def dice(dice_string):
    print(
        safe_dump(
            digest_outcomes(parse_dice(dice_string)),
            default_flow_style=False
        ))
