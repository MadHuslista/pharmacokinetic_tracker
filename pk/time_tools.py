#!/usr/bin/python
# -*- coding: utf-8 -*-

import typing as tp

import numpy as np
from datetime import datetime

from config import START_TIME

# -->> Tunables <<---------------------


# -->> Definitions <<------------------


# -->> API <<--------------------------

def curr_time_to_delay(
    curr_time: np.datetime64,
    start_time: np.datetime64 = START_TIME,
) -> float:
    """Convert current time to delay in hours."""
    delay = curr_time - start_time
    return delay.astype("timedelta64[s]") / np.timedelta64(3600, "s")


# -->> Execute <<----------------------


# -->> Export <<-----------------------

__all__ = [
    "curr_time_to_delay",
]