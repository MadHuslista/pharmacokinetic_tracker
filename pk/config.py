#!/usr/bin/python
# -*- coding: utf-8 -*-

from pathlib import Path
import subprocess

import numpy as np

# -->> Tunables <<---------------------


# -->> Definitions <<------------------

# Paths
REPO_DIR=Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).strip().decode("utf-8"))

# TODO: Change name of this path
DOSAGE_RECORD_PATH= REPO_DIR / "run_pk.sh"
PK_LIB = REPO_DIR / "pk"
DOSES_FILE = "doses.txt"
DELAYS_FILE  = "delays.txt"
DOSES_RECORD_PATH = PK_LIB / DOSES_FILE
DELAYS_FILE_PATH = PK_LIB / DELAYS_FILE

#Dosage Parameters
START_TIME = np.datetime64("2023-09-13T13:50:00")
EFFICACY_THRESHOLD = 0.75
LAST_BOX=np.datetime64("2023-11-22T13:10:00")

# String formatting
CSTM_TAB = "       "
PATTERNS = {
        "%Y-%m-%d %H:%M": r"\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}",  # Matches YYYY-MM-DD-HH:MM
        "%y-%m-%d %H:%M": r"\d{2}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}", # Matches YY-MM-DD HH:MM
        "%m-%d-%H:%M": r"\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}",          # Matches MM-DD-HH:MM
        "%d %H:%M": r"\d{1,2} \d{1,2}:\d{1,2}",                   # Matches DD-HH:MM
        "%H:%M": r"\d{1,2}:\d{1,2}",                              # Matches HH:MM
    }
PATTERNS_STR = ", \n\t".join([i.replace("%", "%%") for i in PATTERNS])
OUTPUT_TIME_FORMAT = f"%Y\n{CSTM_TAB}%d %b\n{CSTM_TAB}%a %H:%M"

# -->> API <<--------------------------


# -->> Execute <<----------------------


# -->> Export <<-----------------------

__all__ = [
    "START_TIME",
    "EFFICACY_THRESHOLD",
]