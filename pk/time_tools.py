#!/usr/bin/python
# -*- coding: utf-8 -*-

import typing as tp

import numpy as np
from datetime import datetime

# -->> Tunables <<---------------------


# -->> Definitions <<------------------

START_TIME = np.datetime64("2023-09-13T13:50:00")

# -->> API <<--------------------------

def curr_time_to_delay(
    curr_time: datetime,
    start_time: datetime = START_TIME,
) -> float:
    """Convert current time to delay in hours."""
    delay = curr_time - start_time
    return delay.astype("timedelta64[s]") / np.timedelta64(3600, "s")


# -->> Execute <<----------------------


# -->> Export <<-----------------------

__all__ = [
    "START_TIME",
    "curr_time_to_delay",
]