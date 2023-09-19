"""Calculates and plots drug concentration over time."""

import argparse

from datetime import datetime 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

import pk
from graph import make_graph

# Use Qt backend for matplotlib so that the window can be resized.
import matplotlib
matplotlib.use('QtAgg')

def simulation(args):
    step = 1/60

    drug = pk.Drug(args.hl, args.tmax)
    num = round(args.duration / step + 1)
    x = np.arange(num) * step
    y = drug.concentration(num, step, dict(zip(args.offsets, args.doses)))

    return x, y

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
    args = ap.parse_args()


    x, y = simulation(args)
    make_graph(x, y, args)

    return 


if __name__ == '__main__':
    main()
