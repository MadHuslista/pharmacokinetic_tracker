#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

# -->> Tunables <<---------------------


# -->> Definitions <<------------------

START_TIME = np.datetime64("2023-09-13T13:50:00")

EFFICACY_THRESHOLD = 0.75


# -->> API <<--------------------------


# -->> Execute <<----------------------


# -->> Export <<-----------------------

__all__ = [
    "START_TIME",
    "EFFICACY_THRESHOLD",
]