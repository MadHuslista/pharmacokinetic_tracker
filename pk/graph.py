#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import typing as tp

from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplcursors
import numpy as np

from time_tools import(
    START_TIME,
    curr_time_to_delay,
)


# Use Qt backend for matplotlib so that the window can be resized.
import matplotlib
matplotlib.use("QtAgg")


# -->> Tunables <<---------------------


# -->> Definitions <<------------------

def custom_annotation(
    sel: mplcursors.Selection,
    x_time: np.array,
) -> None:
    """Create cp, time and delay annotation."""
    cp = round(sel.target[1], 2)
    time = x_time[int(sel.index)]
    delay = curr_time_to_delay(time)

    time_label = time.astype(datetime)
    day_label = datetime.strftime(time_label, "%d-%m-%y")
    time_label = datetime.strftime(time_label, "%H:%M")

    message = (
        f"Day     : {day_label}\n"
        f"Time    : {time_label}\n"
        f"Delay  : {delay:.2f}\n"
        f"Cp       : {cp:.2f}"
    )

    # 'ma' is the matplotlib attribute to set the text alignment in multiline
    # annotations.
    sel.annotation.set(text=message, ma="left")


# -->> API <<--------------------------


def make_graph(
    x_time: np.array,
    drug_cp: np.array,
    args: argparse.Namespace,
) -> None:
    """Make graph of drug concentration over time."""
    plt.rcParams["font.size"] = 12

    fig_width = args.output_size[0] / args.dpi
    fig_height = args.output_size[1] / args.dpi
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), tight_layout=True)

    drug_curve = ax.plot(x_time, drug_cp)

    # Addition of x axis time format
    x_formatter = mdates.DateFormatter("%H:%M %d-%m-%y")
    ax.xaxis.set_major_formatter(x_formatter)

    x_hourlocator = mdates.HourLocator(byhour=[0, 12])
    # x_daylocator = mdates.DayLocator(interval=1)
    ax.xaxis.set_major_locator(x_hourlocator)
    # ax.xaxis.set_minor_locator(x_hourlocator)
    ax.xaxis.set_tick_params(rotation=-90)

    # Add effectiveness threshold
    threshold = 0.75
    ax.hlines(
        threshold,
        *ax.get_xlim(),
        color="red",
        linestyles="dashed",
        label=f"Effectiveness Threshold: \n{threshold}",
    )

    # Addition of current time marker
    now = datetime.now()
    current_time = np.datetime64(now)
    current_time_label = datetime.strftime(now, "%H:%M %d-%m-%y")
    ax.vlines(
        current_time,
        *ax.get_ylim(),
        color="red",
        linestyles="dashed",
        label=f"Current Time: \n{current_time_label}",
    )

    # Addition of current delay label
    # delay = current_time - START_TIME
    # current_delay = delay.astype('timedelta64[s]')/np.timedelta64(3600, 's')
    current_delay = curr_time_to_delay(curr_time=current_time)
    current_delay_label = f"Current Delay: \n{current_delay:.2f} hours"
    ax.scatter(current_time, 0, label=current_delay_label, s=0)

    ax.set_xlabel("Hours", fontsize=18)
    ax.set_ylabel("Concentration", fontsize=18)
    ax.grid(linestyle="--")
    ax.legend()
    ax.margins(0.025, 0.05)
    ax.autoscale()

    # Add Hover cursor
    cursor = mplcursors.cursor(drug_curve, hover=2)
    cursor.connect(
        "add",
        lambda sel: custom_annotation(sel, x_time=x_time),
    )

    fig.savefig(args.output, dpi=args.dpi)
    fig.show()



# -->> Execute <<----------------------


# -->> Export <<-----------------------

__all__ = ["make_graph"]
