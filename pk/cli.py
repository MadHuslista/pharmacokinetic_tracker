#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from datetime import datetime

import numpy as np
import texttable as tt

from config import (
    START_TIME,
    EFFICACY_THRESHOLD,
    PATTERNS_STR,
)

from time_tools import (
    curr_time_to_delay,
)

# -->> Tunables <<---------------------


# -->> Definitions <<------------------


def print_table(
    data: list,
) -> None:
    """Print table."""
    table = tt.Texttable()
    table.add_rows(data, header=True)
    print("\nDosage Info:")
    message = table.draw()
    print(message)


# -->> API <<--------------------------

def arg_parser() -> argparse.ArgumentParser:
    """Create argument parser."""

    # Create argument parser
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    ap.add_argument('--hl', type=float, required=True, metavar='HOURS',
                    help='the drug\'s elimination half-life, in hours')
    ap.add_argument('--tmax', type=float, required=True, metavar='HOURS',
                    help='the drug\'s time to maximum concentration, in hours')
    ap.add_argument('--duration', type=float, default=24, metavar='HOURS',
                    help='the duration, in hours, to simulate concentrations for')
    ap.add_argument('--doses', type=float, nargs='+', default=[1], metavar='DOSE',
                    help='the magnitudes of each dose (units are arbitrary)')
    ap.add_argument('--offsets', type=float, nargs='+', default=[0], metavar='OFFSET',
                    help='the time, in hours, that each dose is given at')
    ap.add_argument('--output', default='output.png', metavar='FILE',
                    help='the output image filename')
    ap.add_argument('--output-size', type=int, nargs=2, default=[1920, 1280], metavar=('W', 'H'),
                    help='the output width and height in pixels')
    ap.add_argument('--dpi', type=float, default=160, help='the output dots per inch (dpi)')
    ap.add_argument('-g', '--graph', action='store_true', help='show the graph')

    ap.add_argument('-p','--parsetime', nargs='*', type=str, help=f"parse a time string and exit. Accepted formats: {PATTERNS_STR}")

    return ap.parse_args()



def cli_message(
    offsets: list,
    x_time: np.array,
    drug_cp: np.array,
) -> None:
    """Add CLI info in the following format.

    | Last dosage time:       | Current time:            |
    | - 2021-03-01 12:00:00   | - 2021-03-01 12:00:00    |
    | Last dosage delay:      | Current delay:           |
    | - 0                     | - 0                      |
    | Time of next dosage:    | Current cp:              |
    | - 2021-03-01 12:00:00   | - 0.5                    |
    """
    # Last dosage delay
    last_dosage_delay = offsets[-1]

    # Last dosage time
    last_dosage_time = START_TIME + np.timedelta64(int(last_dosage_delay * 3600), "s")
    last_dosage_time_day_label = datetime.strftime(
        last_dosage_time.astype(datetime),
        "%d-%m-%y",
    )
    last_dosage_time_hour_label = datetime.strftime(
        last_dosage_time.astype(datetime),
        "%H:%M",
    )

    # Last dosage CP
    last_dosage_idx = np.abs(x_time - last_dosage_time).argmin()
    last_dosage_cp = drug_cp[last_dosage_idx]

    # Current Time
    current_time = datetime.now()
    current_time_day_label = datetime.strftime(current_time, "%d-%m-%y")
    current_time_hour_label = datetime.strftime(current_time, "%H:%M")

    # Current delay
    current_time_np64 = np.datetime64(current_time)
    curr_delay = curr_time_to_delay(current_time_np64)

    # Current CP
    current_cp_idx = np.abs(x_time - current_time_np64).argmin()
    current_cp = drug_cp[current_cp_idx]

    # Max CP since last dosage
    last_dosage_max_idx = drug_cp[last_dosage_idx:].argmax() + last_dosage_idx
    last_dosage_max_cp = drug_cp[last_dosage_max_idx]

    # Max CP time since last dosage
    last_dosage_max_time = x_time[last_dosage_max_idx]
    last_dosage_max_time_day_label = datetime.strftime(
        last_dosage_max_time.astype(datetime),
        "%d-%m-%y",
    )
    last_dosage_max_time_hour_label = datetime.strftime(
        last_dosage_max_time.astype(datetime),
        "%H:%M",
    )

    #Max CP delay since last dosage
    last_dosage_max_delay = curr_time_to_delay(last_dosage_max_time)

    # Next dosage time
    next_dosage_idx = (
        np.abs(drug_cp[last_dosage_max_idx:] - EFFICACY_THRESHOLD).argmin() + last_dosage_max_idx
    )

    next_dosage_time = x_time[next_dosage_idx]

    next_dosage_time_day_label = datetime.strftime(
        next_dosage_time.astype(datetime),
        "%d-%m-%y",
    )
    next_dosage_time_hour_label = datetime.strftime(
        next_dosage_time.astype(datetime),
        "%H:%M",
    )

    # Next dosage delay
    next_dosage_delay = curr_time_to_delay(next_dosage_time)

    # Print CLI message
    data = [
        ["Last Dose", "Max Dose", "Current Dose", "Next Threshold cross"],
        [
            f"Time:\n\t{last_dosage_time_day_label}\n\t{last_dosage_time_hour_label}",
            f"Time:\n\t{last_dosage_max_time_day_label}\n\t{last_dosage_max_time_hour_label}",
            f"Time:\n\t{current_time_day_label}\n\t{current_time_hour_label}",
            f"Time:\n\t{next_dosage_time_day_label}\n\t{next_dosage_time_hour_label}",
        ],
        [
            f"Delay:\n\t{last_dosage_delay}",
            f"Delay:\n\t{last_dosage_max_delay}",
            f"Delay:\n\t{curr_delay:.2F}",
            f"Delay:\n\t{next_dosage_delay:.2F}",
        ],
        [
            f"CP:\n\t{last_dosage_cp:.2F}",
            f"CP:\n\t{last_dosage_max_cp:.2F}",
            f"CP:\n\t{current_cp:.2F}",
            "",
            # f"CP:\n\t{next_dosage_cp:.2F}",
        ],
    ]

    print_table(data)


# -->> Execute <<----------------------


# -->> Export <<-----------------------
