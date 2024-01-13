"""Calculates and plots drug concentration over time."""

import typing as tp

import numpy as np

from cli import (
    arg_parser,
    cli_message,
)
from config import START_TIME

from db import (
    open_record,
)

from graph import make_graph
from time_tools import parse_input_time
import pk


# Use Qt backend for matplotlib so that the window can be resized.
import matplotlib
matplotlib.use('QtAgg')

# -->> Tunables <<---------------------


# -->> Definitions <<------------------

def run_estimation(
    half_life: float,
    time_to_max: float,
    estimation_duration: float,
    doses: list,
    offsets: list,
) -> tp.Tuple[np.array, np.array, np.array]:
    """Wrapper to calculate drug concentration over time."""
    step = 1/60

    # TODO: Move to a dedicated module apart from pk.py

    print("Calculating drug concentration over time...")
    drug = pk.Drug(half_life, time_to_max)
    num = round(estimation_duration / step + 1)
    x_hours = np.arange(num) * step
    drug_cp = drug.concentration(num, step, dict(zip(offsets, doses)))

    x_sec = x_hours * 3600
    x_time = x_sec.astype("timedelta64[s]") + START_TIME

    return x_sec, x_time, drug_cp

# -->> API <<--------------------------

def main():
    """The main function."""

    args = arg_parser()

    if args.parsetime != None:  #--parsetime = -p
        parse_input_time(args.parsetime)
        return
    
    if args.record:
        open_record()
        return
    
    x_sec, x_time, drug_cp = run_estimation(
        half_life=args.hl,
        time_to_max=args.tmax,
        estimation_duration=args.duration,
        doses=args.doses,
        offsets=args.offsets,
    )

    cli_message(
        offsets=args.offsets,
        x_time=x_time,
        drug_cp=drug_cp,
    )

    if args.graph:
        make_graph(x_time, drug_cp, args)
        

# -->> Execute <<----------------------

if __name__ == '__main__':
    main()

# -->> Export <<-----------------------

__all__ = [
    "main",
]