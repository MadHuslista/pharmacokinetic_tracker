
import argparse
import typing as tp

from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np




# Use Qt backend for matplotlib so that the window can be resized.
import matplotlib
matplotlib.use('QtAgg')


def make_graph(x, y, args):

    plt.rcParams['font.size'] = 12

    fig_width = args.output_size[0] / args.dpi
    fig_height = args.output_size[1] / args.dpi
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), tight_layout=True)

    # Addition of start time to x axis
    start_time = np.datetime64('2023-09-13T13:50:00')
    x_sec = x * 3600 
    x_time = x_sec.astype('timedelta64[s]') + start_time
    ax.plot(x_time, y)

    # Addition of x axis time format
    x_formatter = mdates.DateFormatter('%H:%M %d-%m-%y')
    ax.xaxis.set_major_formatter(x_formatter)

    # x_daylocator = mdates.DayLocator(interval=1)
    x_hourlocator = mdates.HourLocator(byhour=[0,12])

    ax.xaxis.set_major_locator(x_hourlocator)
    # ax.xaxis.set_minor_locator(x_hourlocator)
    ax.xaxis.set_tick_params(rotation=-90)

    # Add effectiveness threshold 
    threshold = 0.75
    ax.hlines(threshold, *ax.get_xlim(), color='red', linestyles='dashed', label=f'Effectiveness Threshold: \n{threshold}')

    # Addition of current time marker    
    now = datetime.now()
    current_time = np.datetime64(now)
    current_time_label = datetime.strftime(now, '%H:%M %d-%m-%y')
    ax.vlines(current_time, *ax.get_ylim(), color='red', linestyles='dashed', label=f'Current Time: \n{current_time_label}')

    #Addition of current delay label 
    delay = current_time - start_time
    current_delay = delay.astype('timedelta64[s]')/np.timedelta64(3600, 's') 
    current_delay_label = f"Current Delay: \n{current_delay:.2f} hours"
    ax.scatter(current_time, 0, label=current_delay_label, s=0)

    ax.set_xlabel('Hours', fontsize=18)
    ax.set_ylabel('Concentration', fontsize=18)
    ax.grid(linestyle='--')
    ax.legend()
    # hour_tick_steps = [1, 1.2, 1.6, 1.68, 2, 2.4, 3, 4, 4.8, 6, 8, 9.6, 10]
    # ax.xaxis.set_major_locator(plt.MaxNLocator(nbins='auto', integer=True, steps=hour_tick_steps))
    ax.margins(0.025, 0.05)
    ax.autoscale()
    fig.savefig(args.output, dpi=args.dpi)
    fig.show()
    input('Press enter to exit...')
