"""Calculates and plots drug concentration over time."""

import argparse
import typing as tp

import numpy as np

from cli import cli_message
from config import START_TIME
from graph import make_graph
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
    ap.add_argument('--graph', action='store_true', help='show the graph')
    args = ap.parse_args()


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