#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

import numpy as np
import texttable as tt

from config import (
    START_TIME,
    EFFICACY_THRESHOLD,
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

    # Next dosage time
    last_dosage_idx = np.abs(x_time - last_dosage_time).argmin()
    last_dosage_max_idx = drug_cp[last_dosage_idx:].argmax() + last_dosage_idx

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

    # Next dosage CP
    next_dosage_cp = drug_cp[next_dosage_idx]

    # Print CLI message
    data = [
        ["Last Dose", "Current Dose", "Next Threshold cross"],
        [
            f"Time:\n\t{last_dosage_time_day_label}\n\t{last_dosage_time_hour_label}",
            f"Time:\n\t{current_time_day_label}\n\t{current_time_hour_label}",
            f"Time:\n\t{next_dosage_time_day_label}\n\t{next_dosage_time_hour_label}",
        ],
        [
            f"Delay:\n\t{last_dosage_delay}",
            f"Delay:\n\t{curr_delay:.2F}",
            f"Delay:\n\t{next_dosage_delay:.2F}",
        ],
        [
            f"CP:\n\t{last_dosage_cp:.2F}",
            f"CP:\n\t{current_cp:.2F}",
            "",
            # f"CP:\n\t{next_dosage_cp:.2F}",
        ],
    ]

    print_table(data)


# -->> Execute <<----------------------


# -->> Export <<-----------------------
