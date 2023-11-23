#!/usr/bin/python
# -*- coding: utf-8 -*-

import typing as tp
import re
import numpy as np
from datetime import datetime

from config import START_TIME

# -->> Tunables <<---------------------


# -->> Definitions <<------------------

FORMAT = "%Y-%m-%d %H:%M"

# -->> API <<--------------------------

def curr_time_to_delay(
    curr_time: np.datetime64,
    start_time: np.datetime64 = START_TIME,
) -> float:
    """Convert current time to delay in hours."""
    delay = curr_time - start_time
    return delay.astype("timedelta64[s]") / np.timedelta64(3600, "s")

def detect_input_time_format(
    input_time: str,
) -> str:
    
    patterns = {
        "%Y-%m-%d %H:%M": r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}",  # Matches YYYY-MM-DD-HH:MM
        "%y-%m-%d %H:%M": r"\d{2}-\d{2}-\d{2} \d{2}:\d{2}", # Matches YY-MM-DD HH:MM
        "%m-%d-%H:%M": r"\d{2}-\d{2} \d{2}:\d{2}",          # Matches MM-DD-HH:MM
        "%d-%H:%M": r"\d{2} \d{2}:\d{2}",                   # Matches DD-HH:MM
        "%H:%M": r"\d{2}:\d{2}",                              # Matches HH:MM
    }

    for time_format, pattern in patterns.items():
        if re.match(pattern, input_time):
            # Print the detected time format
            print(f"Detected time format: {time_format}")
            return time_format
    
    # If no time format is detected, return None and print an error message
    print(f"Error: Could not detect time format for input time: {input_time}")
    return None

def edit_input_time(
    input_time: datetime,
) -> datetime:
    """Edit input time string."""
    while True: 
        print(f"Input time: {input_time}")
    
        component_to_edit = input ("Edit any component? (y/m/d/H/M): ")
        components = ['y', 'm', 'd', 'H', 'M']    

        if component_to_edit in components:
            # Ask user for new value
            new_value = input("New value: ")

            # Update the input time
            if component_to_edit == "y":
                input_time = input_time.replace(year=int(new_value))
            elif component_to_edit == "m":
                input_time = input_time.replace(month=int(new_value))
            elif component_to_edit == "d":
                input_time = input_time.replace(day=int(new_value))
            elif component_to_edit == "H":
                input_time = input_time.replace(hour=int(new_value))
            elif component_to_edit == "M":
                input_time = input_time.replace(minute=int(new_value))
            else:
                print(f"Error: Invalid component: {component_to_edit}")
        else:
            break
    return input_time

def parser(
        input_time_str: str,
) -> np.datetime64:
    
    current_datetime = datetime.now()

    input_format = detect_input_time_format(input_time_str)

    # Fill missing components from current datetime
    if "%Y" not in input_format and "%y" not in input_format:
        input_time_str = f"{current_datetime.year}-{input_time_str}"
        input_format = f"%Y-{input_format}"
    if "%m" not in input_format:
        input_time_str = f"{current_datetime.strftime('%m')}-{input_time_str}"
        input_format = f"%m-{input_format}"
    if "%d" not in input_format:
        input_time_str = f"{current_datetime.strftime('%d')}-{input_time_str}"
        input_format = f"%d-{input_format}"

    # Handle two-digit year format
    if "%y" in input_format:
        input_time_str = f"20{input_time_str}"
        input_format = input_format.replace("%y", "%Y")
    
    # Parse the time string
    parsed_time = datetime.strptime(input_time_str, input_format)

    # Edit the time string
    parsed_time = edit_input_time(parsed_time)
    
    # Convert to numpy.datetime64
    return np.datetime64(parsed_time)

def parse_input_time(
    input_time_str: str,
) -> None:
    """Parse input time string and print delay."""
    input_time = parser(input_time_str)
    delay = curr_time_to_delay(input_time)
    print(f"Delay: {delay:.2f} hours")

# -->> Execute <<----------------------

if __name__ == '__main__': 

    input_time = input("Input time: ")
    parse_input_time(input_time)


# -->> Export <<-----------------------

__all__ = [
    "curr_time_to_delay",
]