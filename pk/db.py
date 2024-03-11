#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess as sp

from config import (
    DOSAGE_RECORD_PATH,
)

# -->> Tunables <<---------------------


# -->> Definitions <<------------------


# -->> API <<--------------------------

def open_record(): 
    """Open dosage record."""
    sp.run(["code", "-n", DOSAGE_RECORD_PATH], shell=False)


# -->> Execute <<----------------------


# -->> Export <<-----------------------
