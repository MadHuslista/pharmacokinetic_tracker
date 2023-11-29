#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

# -->> Tunables <<---------------------


# -->> Definitions <<------------------

START_TIME = np.datetime64("2023-09-13T13:50:00")

EFFICACY_THRESHOLD = 0.75

CSTM_TAB = "       "

PATTERNS = {
        "%Y-%m-%d %H:%M": r"\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}",  # Matches YYYY-MM-DD-HH:MM
        "%y-%m-%d %H:%M": r"\d{2}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}", # Matches YY-MM-DD HH:MM
        "%m-%d-%H:%M": r"\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}",          # Matches MM-DD-HH:MM
        "%d %H:%M": r"\d{1,2} \d{1,2}:\d{1,2}",                   # Matches DD-HH:MM
        "%H:%M": r"\d{1,2}:\d{1,2}",                              # Matches HH:MM
    }

# Create a string with the PATTERNS dict keys
PATTERNS_STR = ", \n\t".join([i.replace("%", "%%") for i in PATTERNS])

OUTPUT_TIME_FORMAT = f"%Y\n{CSTM_TAB}%d %b\n{CSTM_TAB}%a %H:%M"

# -->> API <<--------------------------


# -->> Execute <<----------------------


# -->> Export <<-----------------------

__all__ = [
    "START_TIME",
    "EFFICACY_THRESHOLD",
]